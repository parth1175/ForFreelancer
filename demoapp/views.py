from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from demoapp.models import data
from demoapp.forms import UploadBookForm
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import re
from bs4 import BeautifulSoup
from django.template import loader
from django.urls import reverse


@csrf_exempt
def home(request):
    num1=0
    num2=0
    company = ""
    job = ""

    if request.method == 'POST':
        reqs = request.body.decode('utf-8')
        try:
            reqs[:5]

            status = reqs.split('\n', 1)[0]
            print(status)
            rest = reqs.split('\n', 1)[1]

            username = rest.split('\n', 1)[0]  #######################################
            print(username)
            rest2 = rest.split('\n', 1)[1]

            url = rest2.split('\n', 1)[0]  #############################
            print(url)
            textNotes = rest2.split('\n', 1)[1]

            notes = textNotes.split('\n', 1)[0]  #############################
            print(notes)
            text = textNotes.split('\n', 1)[1]


            rawSite = re.search("^(?:https?:\/\/)?(?:[^@\/\n]+@)?(?:www\.)?([^:\/?\n]+)", url)
            SiteName = rawSite.group(1)

            #processing ti retrieve the company name/job title

            # result = re.search('<title>(.*) | LinkedIn</title>', htmlText)
            # try:
            #     companyJob = result.group(1)
            #     companyJob = companyJob[4:]
            #     companyJob = companyJob[:-2]
            #
            # except AttributeError:
            #     companyJob= result
            # print(companyJob)
            #
            # job = (companyJob.split('|', 1)[0])[:-1]  ################################
            # company = (companyJob.split('|', 1)[1])[1:]
            # #processing to retrieve the description
            # num1 = text.find('<!----> <span>')
            # num2 = text.find('<!----> </span>', num1)
            # soup = BeautifulSoup (htmlText[num1:num2], 'html.parser')
            # # subtext = (soup.get_text('\n','\n\n')).replace('\n', '')
            # subtext = soup.get_text(strip=True)
            # shortened_subtext = subtext[:200] + "..."
            # print(subtext[:100])

            handshake_identifier = "handshake-production-cdn"
            linkedin_identifier = "linkedin-logo"
            zip_identifier = "www.ziprecruiter.com"
            indeed_identifier = "indeed_gnav"
            meta_identifier = "About Meta"

            if linkedin_identifier in text:
                num1 = text.find('<!----> <span>')
                print("num1")
                print(num1)
                num2 = text.find('<!----> </span>', num1)
                print("num2")
                print(num2)
                result = re.search('<title>(.*)| LinkedIn</title>', text)
                try:
                    companyJob = result.group(1)
                    companyJob = companyJob[4:]
                    companyJob = companyJob[:-18]
                except AttributeError:
                    companyJob = result
                job = (companyJob.split('|', 1)[0])[:-1]  ################################
                company = (companyJob.split('|', 1)[1])[1:]
                print(companyJob)

            elif handshake_identifier in text:
                peer_exp = '<h2 class="style__heading___3liBJ style__heading___29i1Z style__large___15W-p">Ask a peer about their experience'
                if peer_exp in text:
                    num1 = text.find('<h2 class="style__role-description-title___2aHXu style__heading___29i1Z style__large___15W-p">')
                    num2 = text.find(peer_exp)
                else:
                    num1 = text.find('<h2 class="style__role-description-title___2aHXu style__heading___29i1Z style__large___15W-p">')
                    num2 = text.find('class="style__container___L2N8n"><h2 class="style__title___1Smoz style__heading___29i1Z style__large___15W-p">')
                result = re.search('<title>(.*)| Handshake</title>', text)
                try:
                    companyJob = result.group(1)
                    companyJob = companyJob[4:]
                    companyJob = companyJob[:-20]
                except AttributeError:
                    companyJob = result
                job = (companyJob.split('|', 1)[0])[:-1]
                company = (companyJob.split('|', 1)[1])[1:]
                print(job)
                print(company)

            elif zip_identifier in text:
                num1 = text.find('<div class="jobDescriptionSection">')
                num2 = text.find('<p class="report_job">')
                result = re.search('"hiring_company_text t_company_name">(.*) </span>', text)
                soup = BeautifulSoup(result.group(1), 'html.parser')
                company = (soup.get_text('\n','\n\n')).replace('\n', ' ')
                print(company)
                dragondese = re.search("name: '(.*)',\nlocation:", text)
                job = dragondese.group(1)
                print(job)

            elif meta_identifier in text:
                num1 = text.find('<div class="_3gel _3gfe _3gef _3gee _8lfv _3-8p _8lfv _3-8p"><div class="_25x1 _25x7 _25xj _1ilv _1iot _38g3 _3geg _38g4 _38g5" style="background-color: ">')
                num2 = text.find('<div class="_97fe _1n-z _6hy- _8lfs">Locations')
                result = re.search('<meta property="og:title" content="(.*)"><meta property="og:description"', text)
                soup = BeautifulSoup(result.group(1), 'html.parser')
                job = (soup.get_text('\n','\n\n')).replace('\n', ' ')
                print(job)
                company = "Meta"
                print(company)



            soup = BeautifulSoup(text[num1:num2], 'html.parser')
            subtext = (soup.get_text('\n','\n\n')).replace('\n', ' ')
            print(subtext)
            shortened_subtext = subtext[:200] + "..."
            print(subtext[:100])



















            # print(subtext)

            #Unique = True
            #for i in data.objects.all():
            #    if(i.Company == company or i.Job == job):
            #        print("duplicate found!")
            #        Unique = False
            #        break
            #if(Unique==True):
            p = data(user=username, Website=SiteName, Notes =notes, Url=url, Company=company, Description=shortened_subtext, Job = job, Applied = status)
            p.save()

            return JsonResponse(
                {
                "success":True,
                "url": reqs[:5]
                }
            )
        except KeyError:
            print("wrong!")
            #raise JsonInvalidError

    else:
        datas = data.objects.all()

        return render(request,'demoapp/htmlcode.html',{'datas':datas})
# Create your views here.

def update_data(request, data_id):
    updata = data.objects.get(id=data_id)
    template = loader.get_template('Update/update.html')
    context = {
        'updata': updata,
    }

    return HttpResponse(template.render(context, request))

def updaterecord(request, data_id):
    url = request.POST['url']
    company = request.POST['company']
    job = request.POST['job']
    description = request.POST['description']
    notes = request.POST['notes']
    applied = request.POST['applied']
    #date = request.POST['date']
    data1 = data.objects.get(id=data_id)
    data1.url = url
    data1.Company = company
    data1.Job = job
    data1.Description = description
    data1.Notes = notes
    data1.Applied = applied
    #data1.Date = date
    data1.save()
    return redirect('/')
    #return HttpResponseRedirect(reverse('htmlcode'))

def delete(request, id):
  data2 = data.objects.get(id=id)
  data2.delete()
  return redirect('/')
  #return HttpResponseRedirect(reverse('index'))

def add(request):
  template = loader.get_template('Add/add.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
    username = request.user.username
    url = request.POST['url']
    website = request.POST['website']
    company = request.POST['company']
    job = request.POST['job']
    description = request.POST['description']
    notes = request.POST['notes']
    applied = request.POST['applied']
    data2 = data(user=username, Url=url, Website=website, Company=company, Job=job, Description=description, Notes=notes, Applied=applied)
    data2.save()
    return redirect('/')

def resume(request):
    template = loader.get_template('Resume/resume.html')
    return HttpResponse(template.render({}, request))

def BookUploadView(request):
    if request.method == 'POST':
        form = UploadBookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('The file is saved')
    else:
        form = UploadBookForm()
        context = {
            'form':form,
        }
    return render(request, 'Resume/resume.html', context)

def privacy(request):
    template = loader.get_template('Privacy/privacy.html')
    return HttpResponse(template.render({}, request))
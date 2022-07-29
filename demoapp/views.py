from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from demoapp.models import data
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import re
from bs4 import BeautifulSoup
from django.template import loader
from django.urls import reverse


@csrf_exempt
def home(request):

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
            text = rest2.split('\n', 1)[1]

            notes = text.split('\n', 1)[0]  #############################
            print(notes)
            htmlText = text.split('\n', 1)[1]

            #processing ti retrieve the company name/job title

            result = re.search('<title>(.*) | LinkedIn</title>', htmlText)
            try:
                companyJob = result.group(1)
                companyJob = companyJob[4:]
                companyJob = companyJob[:-2]

            except AttributeError:
                companyJob= result
            print(companyJob)
            job = (companyJob.split('|', 1)[0])[:-1]  ################################
            company = (companyJob.split('|', 1)[1])[1:]
            #processing to retrieve the description
            num1 = text.find('<!----> <span>')
            num2 = text.find('<!----> </span>', num1)
            soup = BeautifulSoup (htmlText[num1:num2], 'html.parser')
            # subtext = (soup.get_text('\n','\n\n')).replace('\n', '')
            subtext = soup.get_text(strip=True)
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
            p = data(user=username, Notes =notes, Url=url, Company=company, Description=shortened_subtext, Job = job, Applied = status)
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

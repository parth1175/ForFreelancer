from django.shortcuts import render
from django.http import HttpResponse
from demoapp.models import data
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import re
from bs4 import BeautifulSoup


@csrf_exempt
def home(request):

    if request.method == 'POST':
        reqs = request.body.decode('utf-8')
        #reqs = request.body
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
            subtext = (soup.get_text('\n','\n\n')).replace('\n', '')
            # print(subtext)

            p = data(user=username, Notes =notes,  url=url, Company=company, Description=subtext, Job = job, Status=status)
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

        #send = data.objects.create(user = 'rohanchitrao',url = url, Company_Job=companyJob, Description = subtext )
        #send.save();
        #send = data()
        #send.user = 'rohanchitrao'
        #send.url = url
        #send.Company_Job=companyJob
        #send.Description = subtext
        #send.save()






    else:
        datas = data.objects.all()

        return render(request,'demoapp/htmlcode.html',{'datas':datas})
# Create your views here.

def update_data(request, data_id):
    dataid = data.objects.get(pk=data_id)
    return render(request, 'Update/update.html')
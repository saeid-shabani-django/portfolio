from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage


def home(request):
    return render(request,'home.html')


def about(request):
    return render(request,'about.html')

def projects(request):

    projects_show = [
        {'title':'blog',
         'path':'images/blog.png'},

    ]
    return render(request,'projects.html',{'projects_show':projects_show})


def experiences(request):
    experiences=[
        {'company_name':'abc',
         'position':'python developer'},
    ]
    return render(request,'experience.html',{'experiences':experiences})


def certificates(request):
    return render(request,'certificates.html')


def contact(request):
    return render(request,'contact.html')

def resume(request):
    resume_path = 'resume/resume/SaeidShabaniResume.pdf'
    resume_path = staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path,'rb') as resume_file:
            response = HttpResponse(resume_file.read(),content_type='application/pdf')
            response['Content-Disposition']='attachment';filename='SaeidShabaniResume.pdf'
            return response
    else:
        return HttpResponse('file does not exist')

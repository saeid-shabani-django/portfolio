from django.shortcuts import render

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







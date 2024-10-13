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




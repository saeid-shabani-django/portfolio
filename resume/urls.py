from django.urls import  path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('projects/',views.projects,name='projects'),
    path('experiences/',views.experiences,name='experiences'),
    path('certificates/',views.certificates,name='certificates'),

]

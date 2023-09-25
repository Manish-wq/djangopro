from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.empty, name='empty'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('work', views.work, name='work'),
    path('causes', views.causes, name='causes'),
    path('blogs', views.blogs, name='blogs'),
    path('contact', views.contact, name='contact'),
    path('community', views.community, name='community')
]
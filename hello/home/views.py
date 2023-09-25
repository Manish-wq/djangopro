from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Community
from django.contrib import messages

# Create your views here.
def empty(request):
    context = {
        'variable1':'This is me The Futurist',
        'variable2':'This is me The Futurist and Philosopher'
    }
    return render(request, 'index.html', context)
    # return HttpResponse('Welcome back index')


def home(request):
     return render(request, 'home.html')
    


def about(request):
 return render(request, 'about.html')
    

def work(request):
 return render(request, 'work.html')
    

def causes(request):
 return render(request, 'causes.html')
    


def blogs(request):
 return render(request, 'blogs.html')


def contact(request):
 return render(request, 'contact.html')

def community(request):
 if request.method == 'POST':
   name = request.POST.get( 'name')
   email = request.POST.get( 'email')
   phone = request.POST.get( 'phone')
   desc = request.POST.get( 'desc')
   community = Community(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
   community.save()
   messages.success(request, 'Your message has been sent!')
 return render(request, 'community.html')
    

from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.

def login(request):
     return render(request, 'registration/login.html', {'section':'main'})

@login_required
def mainpage(request):
    return render(request, 'registration/mainpage.html')

def homepage(request):
    return render(request, 'home/homepage.html')


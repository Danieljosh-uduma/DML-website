from django.shortcuts import render

# Create your views here.
def contact(request):
    return render(request, 'contact/contact.html')

def about(request):
    return render(request, 'about/about.html')

def membership(request):
    return render(request, 'membership/member.html')
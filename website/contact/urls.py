from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('contact/', views.contact, name='homepage'),
    path('membership_info/', views.membership, name='member'),
    path('about/', views.about, name='about'),
]
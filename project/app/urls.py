from django.urls import path
from .views import *

urlpatterns=[
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('category/',category,name='category'),
    path('services/',services,name='services'),
    path('contact/',contact,name='contact'),
    path('register/',register,name='register'),
    path('login/',login,name='login'),
    path('savedata/',savedata,name='savedata'),
    path('dashlogin/',dashlogin,name='dashlogin'),
    path('logout/',logout,name='logout'),
]
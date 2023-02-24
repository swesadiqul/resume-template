
from django.urls import path
from .views import *

# app_name = AppName

urlpatterns = [
    path('', index, name='home'),
    path('get-in-touch/', contact, name='contact'),
    path('services/', services, name='services'),
]
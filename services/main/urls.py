from django.urls import path
from .views import *

urlpatterns = [path('index', index, name='index'),
               path('about', about, name='about'),
               path('contact', contact, name='contact'),
               path('branch', branch, name='branch'),
               path('login', LoginUser.as_view(), name='login'),
               path('accounts/profile/', order),
               path('<slug:portfolio_slug>', work),
               path('', index),
               ]


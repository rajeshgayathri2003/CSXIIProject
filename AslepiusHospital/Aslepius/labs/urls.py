from . import views
from django.urls import path

urlpatterns =[path('tests', views.tests, name='tests'),
              path('booking', views.booking, name='booking'),
              path('payment', views.payment, name='payment'),
              path('redirect', views.redirect, name='redirect'),
              path('homepage', views.redirect1, name='redirect1'),
              ]
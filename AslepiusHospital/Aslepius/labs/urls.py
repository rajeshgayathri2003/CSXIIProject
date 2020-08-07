from . import views
from django.urls import path

urlpatterns =[path('tests', views.tests, name='tests'),
            ]
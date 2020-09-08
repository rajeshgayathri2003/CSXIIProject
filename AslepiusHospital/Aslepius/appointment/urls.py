from django.urls import path
from . import views

urlpatterns = [path('bookappointment', views.bookappointment, name = 'bookappointment'),]
from django.urls import path
from . import views

urlpatterns = [path('contact', views.contact, name='contact'),
               path('contactthankyou', views.contactthankyou, name='contactthankyou')]
#path('',views.FrontScreen,name='FrontScreen')
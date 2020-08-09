from django.urls import path
from . import views
from login import views as loginviews
from dept import views as deptviews
from contactus import views as contactusviews

urlpatterns =[path('updatepasswd', views.updatepasswd, name='updatepasswd'),
              path('mypage', loginviews.mypage, name='mypage'),
              path('updateprofile', views.updateprofile, name ='updateprofile'),
              path('dept', deptviews.dept, name='dept'),
              path('contact', contactusviews.contact, name='contact'),
              path('updatepasswdlogin', loginviews.updatepasswdlogin, name='updatepasswdlogin')]
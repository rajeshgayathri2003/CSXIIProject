from django.urls import path
from . import views
from login import views as loginviews

urlpatterns =[path('updatepasswd', views.updatepasswd, name='updatepasswd'),
              path('mypage', loginviews.mypage, name='mypage'),
              path('updateprofile',views.updateprofile,name='updateprofile') ]
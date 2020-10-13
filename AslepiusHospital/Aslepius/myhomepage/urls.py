from django.urls import path
from . import views
from login import views as loginviews
from dept import views as deptviews
from contactus import views as contactusviews
from vaccines import views as vaccinesviews
from labs import views as labsviews
from opening import views as openingviews
from appointment import views as aptviews

urlpatterns =[path('updatepasswd', views.updatepasswd, name='updatepasswd'),
              path('mypage', loginviews.mypage, name='mypage'),
              path('updateprofile', views.updateprofile, name ='updateprofile'),
              path('dept', deptviews.dept, name='dept'),
              path('contact', contactusviews.contact, name='contact'),
              path('updatepasswdlogin', loginviews.updatepasswdlogin, name='updatepasswdlogin'),
              path('vaccines', vaccinesviews.vaccines, name = 'vaccines'),
              path('tests', labsviews.tests, name= 'tests'),
              path('faq', openingviews.faq, name= 'faq'),
              path('confirm', aptviews.confirm, name='confirm')]
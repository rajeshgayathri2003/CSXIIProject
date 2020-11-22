from . import views
from login import views as loginviews
from django.urls import path

urlpatterns =[path('tests', views.tests, name='tests'),
              path('booking', views.booking, name='booking'),
              path('payment', views.payment, name='payment'),
              path('redirect', views.redirect, name='redirect'),
              path('mypage', loginviews.mypage, name='mypage'),
              path('login', loginviews.login, name='login'),
              path('cancel', views.cancel, name='cancel'),
              path('confirm', views.confirm, name='confirm')
              ]
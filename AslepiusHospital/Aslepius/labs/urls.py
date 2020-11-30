from . import views
from login import views as loginviews
from django.urls import path

urlpatterns =[path('tests', views.tests, name='tests'),
              path('booking', views.booking, name='booking'),
              path('payment', views.payment, name='payment'),
              path('redirect', views.redirect, name='redirect'),
              path('labs_cancel', views.labs_cancel, name='labs_cancel'),
              path('labs_confirm', views.labs_confirm, name='labs_confirm')
              ]

#path('mypage', loginviews.mypage, name='mypage'),
#path('login', loginviews.login, name='login'),
from django.urls import path
from . import views
from login import views as loginviews
from dept import views as deptviews

urlpatterns = [path('bookappointment', views.bookappointment, name = 'bookappointment'),
               path('booknow', views.booknow, name = 'booknow'),
               path('cancel', views.cancel, name='cancel'),
               path('dept', deptviews.dept, name='dept'),
               path('confirm', views.confirm, name='confrim')]
#path('mypage', loginviews.mypage, name='mypage'),
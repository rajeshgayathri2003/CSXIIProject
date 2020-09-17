from django.urls import path
from . import views
from login import views as loginviews

urlpatterns = [path('bookappointment', views.bookappointment, name = 'bookappointment'),
               path('booknow', views.booknow, name = 'booknow'),
               path('mypage', loginviews.mypage, name='mypage'),
               path('cancel', views.cancel, name='cancel')]
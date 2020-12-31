from django.urls import path
from . import views

from django.urls import path
from . import views
from login import views as loginviews


urlpatterns = [path('vaccines',views.vaccines, name='vaccines'),
               path('birth',views.birth, name='birth'),
               path('two_Months', views.two_Months, name='two_Months'),
               path('four_Months', views.four_Months, name='four_Months'),
               path('six_Months', views.six_Months, name='six_Months'),
               path('nine_twelve_Months', views.nine_twelve_Months, name='nine_twelve_Months'),
               path('fifteen_eighteen_Months', views.fifteen_eighteen_Months, name='fifteen_eighteen_Months'),
               path('two_three_Years', views.two_three_Years, name='two_three_Years'),
               path('five_Years', views.five_Years, name='five_Years'),
               path('seven_seventeen_Years', views.seven_seventeen_Years, name='seven_seventeen_Years'),
               path('book_appointment', views.book_appointment, name= 'book_appointment'),
               path('ThankYou', views.ThankYou, name='ThankYou'),
               path('Payment', views.Payment, name='Payment'),
               path('login', loginviews.login, name='login'),
               path('Vaccine_confirm', views.Vaccine_confirm, name = 'Vaccine_confirm'),
               path('Vaccine_cancel', views.Vaccine_cancel, name = 'Vaccine_cancel'),
               path('Home', views.Home, name = 'Home'),
               path('get_chkbox_value', views.get_chkbox_value, name="get_chkbox_value"),
               ]
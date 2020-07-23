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
               path('ThankYou', views.ThankYou, name='ThankYou'),
               path('login', loginviews.login, name='login'),
               ]
from django.urls import path
from . import views
from login import views as loginviews


urlpatterns = [path('vaccines',views.vaccines, name='vaccines'),
               path('birth',views.birth, name='birth'),
               path('two_Months', views.two_Months, name="two_Months"),
               path('login', loginviews.login, name='login'),
               ]
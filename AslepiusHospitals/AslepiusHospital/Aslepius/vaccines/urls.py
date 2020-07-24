from django.urls import path
from . import views


urlpatterns = [path('vaccines',views.vaccines, name='vaccines')]
"""Aslepius URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from contactus import views as contactusviews
from vaccines import views as vaccinesviews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('opening.urls')),
    path('contact/',contactusviews.contact,name='contact/'),
    path('contactthankyou',contactusviews.contactthankyou, name='contactthankyou'),
    path('vaccines/', include('vaccines.urls')),
    path('dept/',include('dept.urls')),
    path('login/',include('login.urls')),
    path('myhomepage/',include('myhomepage.urls')),
    path('appointment/', include('appointment.urls')),
    path('labs/',include('labs.urls')),
    

]

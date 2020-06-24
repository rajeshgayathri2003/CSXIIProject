from django.urls import path
from . import views
from contactus import views as contactusviews
from vaccines import views as vaccinesviews


urlpatterns = [path('login',views.login, name='login'),path('registration', views.registration, name='registration'),]
'''
urlpatterns = [path('',views.FrontScreen,name='FrontScreen'),path('login',views.login, name='login'),
               path('departments', views.dept, name='departments'),
               path('cardiology', views.cardiology, name='cardiology'),
               path('contact', contactusviews.contact, name='contact'),
               path('registration', views.registration, name='registration'),
               path('dental', views.dental, name='dental'),
               path('dermatology', views.dermatology, name='dermatology'),
               path('endocrinology', views.endocrinology, name='endocrinology'),
               path('diet_and_nutrition', views.diet_and_nutrition, name='diet_and_nutrition'),
               path('ENT', views.ENT, name='ENT'),
               path('General_Physicians', views.General_Physicians, name='General_Physicians'),
               path('gynaecology', views.gynaecology, name='gynaecology'),
               path('nephrology', views.nephrology, name='nephrology'),
               path('neurology', views.neurology, name='neurology'),
               path('opthomology', views.opthomology, name='opthomology'),
               path('paediatrics',views.paediatrics, name='paediatrics'),
               path('ortho',views.ortho, name='ortho'),
               path('psy',views.psy, name='psy'),
               path('pulmo', views.pulmo, name='pulmo'),
               path('vaccines', vaccinesviews.vaccines, name='vaccines'),
               path('BabyBlue', views.BabyBlue, name='BabyBlue'),
               path('Brain_Tumour', views.Brain_Tumour, name='Brain_Tumour'),
               path('covid', views.covid, name='covid'),
               path('heart', views.heart, name='heart'),
               path('KidneyCare', views.KidneyCare, name='KidneyCare'),
               path('KidneyPain', views.KidneyPain, name='KidneyPain'),
               path('contactthankyou',contactusviews.contactthankyou, name='contactthankyou')

              ]
'''

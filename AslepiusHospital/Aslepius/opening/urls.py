from django.urls import path
from . import views
from contactus import views as contactusviews
from vaccines import views as vaccinesviews
from dept import views as deptviews
from login import views as loginviews
from labs import views as labsviews


urlpatterns = [path('',views.FrontScreen,name='FrontScreen'),path('login',loginviews.login, name='login'),
               path('departments', deptviews.dept, name='departments'),
               path('cardiology', deptviews.cardiology, name='cardiology'),
               path('contact', contactusviews.contact, name='contact'),
               path('registration', loginviews.registration, name='registration'),
               path('dental', deptviews.dental, name='dental'),
               path('dermatology', deptviews.dermatology, name='dermatology'),
               path('endocrinology', deptviews.endocrinology, name='endocrinology'),
               path('diet_and_nutrition', deptviews.diet_and_nutrition, name='diet_and_nutrition'),
               path('ENT', deptviews.ENT, name='ENT'),
               path('General_Physicians', deptviews.General_Physicians, name='General_Physicians'),
               path('gynaecology', deptviews.gynaecology, name='gynaecology'),
               path('nephrology', deptviews.nephrology, name='nephrology'),
               path('neurology', deptviews.neurology, name='neurology'),
               path('opthomology', deptviews.opthomology, name='opthomology'),
               path('opthomology', deptviews.opthomology, name='opthomology'),
               path('paediatrics',deptviews.paediatrics, name='paediatrics'),
               path('orthopaedics', deptviews.orthopaedics, name='orthopaedics'),
               path('psychiatry', deptviews.psychiatry, name='v'),
               path('pulmonology', deptviews.pulmonology, name='pulmonology'),
               path('vaccines', vaccinesviews.vaccines, name='vaccines'),
               path('BabyBlue', views.BabyBlue, name='BabyBlue'),
               path('Brain_Tumour', views.Brain_Tumour, name='Brain_Tumour'),
               path('covid', views.covid, name='covid'),
               path('heart', views.heart, name='heart'),
               path('KidneyCare', views.KidneyCare, name='KidneyCare'),
               path('KidneyPain', views.KidneyPain, name='KidneyPain'),
               path('contactthankyou',contactusviews.contactthankyou, name='contactthankyou'),
               path('faq',views.faq, name='faq'),
               path('aboutus', views.aboutus, name='aboutus'),
               path('tests', labsviews.tests, name='tests'),

              ]
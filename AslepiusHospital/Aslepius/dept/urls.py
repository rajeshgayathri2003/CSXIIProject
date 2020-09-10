from django.urls import path
from . import views
from contactus.views import contact
from login import views as loginviews
from appointment import views as aptviews

urlpatterns =[path('departments', views.dept, name='departments'),
               path('cardiology', views.cardiology, name='cardiology'),
               path('contact', contact, name='contact'),
               path('registration',loginviews.registration, name='registration'),
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
               path('orthopaedics',views.orthopaedics, name='orthopaedics'),
               path('psychiatry',views.psychiatry, name='v'),
               path('pulmonology', views.pulmonology, name='pulmonology'),
               path('login', loginviews.login, name='login'),
               path('bookappointment', aptviews.bookappointment, name= 'bookappointment')
              ]
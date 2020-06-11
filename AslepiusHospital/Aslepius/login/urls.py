from django.urls import path
from . import views

urlpatterns = [path('',views.FrontScreen,name='frontscreen'),path('login',views.login, name='login'),
               path('departments', views.dept, name='departments'),
               path('cardiology', views.cardiology, name='cardiology'),
               path('contact', views.contact, name='contact'),
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
               path('pulmo', views.pulmo, name='pulmo')

              ]
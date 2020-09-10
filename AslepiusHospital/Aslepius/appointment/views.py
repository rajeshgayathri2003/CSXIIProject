from django.shortcuts import render
from dept import views as deptviews
from . import models
from dept.models import Departments

def bookappointment(request):
    if request.method == "POST":
        doc_id = request.POST['docid']
        #doc_dict = {'doctorID':doc_id}
        docobj = Departments.objects.get(doctorID = doc_id)
        time_details = models.Availability.objects.get(doctorID = doc_id)
        #print(time_details)
        doc_dict = {'docobject':docobj, 'time': time_details}
        #print("SUCCESS")
        
        return render (request, 'appointment/bookapt.html',doc_dict)
    else:
        return render (request, 'appointment/bookapt.html')

#def booknow(request):
    #if request.method == "POST":
        

   





# Create your views here.

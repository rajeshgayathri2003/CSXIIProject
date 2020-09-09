from django.shortcuts import render
from dept import views as deptviews
from . import models
from dept.models import Departments

def bookappointment(request):
    if request.method == "POST":
        doc_id = request.POST['docid']
        #doc_dict = {'doctorID':doc_id}
        docobj = Departments.objects.get(doctorID = doc_id)
        doc_dict = {'docobject':docobj}
        print("SUCCESS")

        return render (request, 'appointment/bookapt.html',doc_dict)
    else:
        return render (request, 'appointment/bookapt.html')

   





# Create your views here.

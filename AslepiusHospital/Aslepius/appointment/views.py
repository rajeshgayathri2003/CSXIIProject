from django.shortcuts import render
from dept import views as deptviews
from . import models
from dept.models import Departments
from django.core.mail import send_mail


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

def booknow(request):
    if request.method == "POST":
        docID = request.POST['docID']
        patient = request.POST['patient']
        date = request.POST['aptdate']
        time = request.POST['Time']
        B = models.Appointment()
        B.date = date
        B.doctorID = Departments.objects.get(doctorID = docID)
        B.patientID = request.user
        B.time = time
        B.save()
        body = 'Dear {0},\nYour appointment with {1} has been confirmed on {2} at {3}\nPlease be on time.\n Regards,\nTeam Aselpius'.format(request.user.first_name, Departments.objects.get(doctorID = docID).docname, date, time)
        send_mail('Appointment Booked', body,
        'aslepius9@gmail.com', [request.user.email,], fail_silently = False)
        #instance.doctorID = docID
        #instance.patientID = request.user
        #instance.save
        return render(request, 'appointment/appointmentthankyou.html')
    else:
        return render(request, 'appointment/bookapt.html')

        

   





# Create your views here.

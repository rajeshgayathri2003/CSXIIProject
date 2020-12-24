from django.shortcuts import render, redirect
from dept import views as deptviews
from . import models
from dept.models import Departments
from django.core.mail import send_mail
import datetime
from django.contrib import messages

''' This function passes the doctor id of the doctor 
    who the patient wishes to meet to the appointments
    page
'''
def bookappointment(request):
    if request.method == "POST":
        doc_id = request.POST['docid']
        print(doc_id)
        docobj = Departments.objects.get(doctorID = doc_id)
        time_details = models.Availability.objects.get(doctorID = doc_id)
        doc_dict = {'docobject':docobj, 'time': time_details}
        return render (request, 'appointment/bookapt.html',doc_dict)
    else:
        return render (request, 'appointment/bookapt.html')

'''This function books an appointment with the doctor and also checks 
    if the doctor is available at the specified time'''

def booknow(request):
    if request.method == "POST":
        docID = request.POST['docID']
        patient = request.POST['patient']
        date = request.POST['aptdate']
        time = request.POST['Time']
        check1 = check(docID, date, time)
        if not check1:
            messages.info(request,'Doctor is unavailable at the requested time. Please try another day')
            return redirect('dept')
        else:
            B = models.Appointment()
            B.date = date
            B.doctorID = Departments.objects.get(doctorID = docID)
            B.patientID = request.user
            B.time = time
            B.save()
            body = 'Dear {0},\nYour appointment with {1} has been confirmed on {2} at {3}\nPlease be on time.\n Regards,\nTeam Aselpius'.format(request.user.first_name, Departments.objects.get(doctorID = docID).docname, date, time)
            send_mail('Appointment Booked', body,
            'aslepius9@gmail.com', [request.user.email,], fail_silently = False)
            return render(request, 'appointment/appointmentthankyou.html')
    else:
        return render(request, 'appointment/bookapt.html')


'''This function asks you to confirm your cancellation'''
def confirm(request):
    if request.method == "POST":
        aptid = request.POST['aptid']
        obj_delete = models.Appointment.objects.filter(aptid = aptid)
        a_dict = {'aptid' : obj_delete}
        print(a_dict)
    return render(request, 'appointment/confirmcancel.html', a_dict)

'''This function enables the patient to cancel the appointment'''        
def cancel(request):
    if request.method == "POST":
        aptid = request.POST['aptid']
        obj_delete = models.Appointment.objects.get(aptid = aptid)
        obj_delete.delete()
        print("SUCCESS")
        return render(request, 'appointment/cancelapt.html')


'''This function checks if the doctor is available
    during the specified time slot'''
def check(doctorID, date, time):
    availability = models.Availability.objects.get(doctorID = doctorID)
    slot = models.Appointment.objects.filter(time = time)
    day = datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%A')
    val = 0
    for i in slot:
        val+=1
    if availability.dayunavailable1 == day or availability.dayunavailable2 == day:
        return False
    elif val> 5:
        return False
    else:
        return True
    
    


    





# Create your views here.

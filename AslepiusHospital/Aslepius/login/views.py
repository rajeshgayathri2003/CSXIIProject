from django.shortcuts import render
import csv
from datetime import datetime
from . import models
from random import randint

def FrontScreen(request):
    return render(request, 'login/opening.html')


def login(request):
    return render(request,'login/login.html')


def dept(request):
    return render(request, 'login/departments.html')


def cardiology(request):
    return render(request, 'login/cardiology.html')


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['Phone']
        country = request.POST['country']
        message = request.POST['subject']
        date = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        with open('contact.csv', 'a') as csvfile:
            csvwriter=csv.writer(csvfile, lineterminator='\n')
            csvwriter.writerow(["name", name])
            csvwriter.writerow(["phone", phone])
            csvwriter.writerow(["country", country])
            csvwriter.writerow(["message", message])
            csvwriter.writerow(["date", date])
        return render(request, 'login/thankyou.html')
    else:
        return render(request, 'login/contact.html')


def registration(request):
    if request.method == "GET":
        return render(request,'login/registration.html')
    else:
        name = request.POST['name']
        #dob = request.POST['dob']
        #gender = request.POST['gender']  #Please check and make the necessary corrections
        email = request.POST['email']
        passwd = request.POST['passwd']
        #confirmpasswd = request.POST['confirmpasswd']
        #mobile = request.POST['mobile']
        Add1 = request.POST['Add1']
        Add2 = request.POST['Add2']
        Add3 = request.POST['Add3']
        city = request.POST['city']
        state = request.POST['state']
        pincode = request.POST['pincode']

        R = models.Register()
        R.patientid=randint(0,10000)
        R.name = name
        R.dob = "2003-10-25" #Fix
        R.gender = "F" #Fix
        R.email = email
        R.passwd = passwd
        R.confirmpasswd = passwd #Fix
        R.mobile = 81977 #Fix
        R.Add1 = "Add1"
        R.Add2 = "Add2"
        R.Add3 = "Add3"
        # Fix
        R.city = city
        R.state = state
        R.pincode = pincode
        R.save()
        return render(request, 'login/opening.html')


def dental(request):
    return render(request,'login/dental.html')


def dermatology(request):
    return render(request, 'login/dermatology.html')


def endocrinology(request):
    return render(request, 'login/endocrinolgy.html')


def diet_and_nutrition(request):
    return render(request, 'login/diet_and_nutrition.html')


def ENT(request):
    return render(request,'login/ENT.html')


def General_Physicians(request):
    return render(request, 'login/General_Physicians.html')


def gynaecology(request):
    return render(request, 'login/Gynaecology.html')


def nephrology(request):
    return render(request,'login/nephrology.html')


def neurology(request):
    return render(request,'login/neurology.html')


def opthomology(request):
    return render(request,'login/opthamology.html')


def paediatrics(request):
    return render(request,'login/paediatrics.html')


def ortho(request):
    return render(request,'login/orthopaedics.html')


def psy(request):
    return render(request,'login/psychiatry.html')


def pulmo(request):
    return render(request, 'login/pulmonology.html')

def vaccines(request):
    return render(request,'login/vaccines.html')

def covid(request):
    return render(request, 'login/Covid19.html')

def BabyBlue(request):
    return render(request, 'login/BlueBabySyndrome.html')

def Brain_Tumour(request):
    return render(request, 'login/Brain_Tumour.html')

def heart(request):
    return render(request, 'login/HeartHealth.html')


def KidneyCare(request):
    return render(request,'login/KidneyCancer.html')

def KidneyPain(request):
    return render(request, 'login/KidneyPain.html')

def contactthankyou(request):
    return render(request,'login/thankyou.html')
# Create your views here.

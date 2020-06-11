from django.shortcuts import render


def FrontScreen(request):
    return render(request, 'login/opening.html')


def login(request):
    return render(request,'login/login.html')


def dept(request):
    return render(request, 'login/departments.html')


def cardiology(request):
    return render(request, 'login/cardiology.html')


def contact(request):
    return render(request, 'login/contact.html')


def registration(request):
    return render(request,'login/registration.html')


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
    return render(request,'login/opthomology.html')


def paediatrics(request):
    return render(request,'login/paediatrics.html')


def ortho(request):
    return render(request,'login/orthopaedics.html')


def psy(request):
    return render(request,'login/psychiatry.html')


def pulmo(request):
    return render(request, 'login/pulmonology.html')
# Create your views here.

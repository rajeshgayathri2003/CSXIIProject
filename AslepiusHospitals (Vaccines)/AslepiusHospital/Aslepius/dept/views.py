from django.shortcuts import render


def dept(request):
    return render(request, 'dept/departments.html')


def cardiology(request):
    return render(request, 'dept/cardiology.html')


def dental(request):
    return render(request, 'dept/dental.html')


def dermatology(request):
    return render(request, 'dept/dermatology.html')


def endocrinology(request):
    return render(request, 'dept/endocrinolgy.html')


def diet_and_nutrition(request):
    return render(request, 'dept/diet_and_nutrition.html')


def ENT(request):
    return render(request, 'dept/ENT.html')


def General_Physicians(request):
    return render(request, 'dept/General_Physicians.html')


def gynaecology(request):
    return render(request, 'dept/Gynaecology.html')


def nephrology(request):
    return render(request, 'dept/nephrology.html')


def neurology(request):
    return render(request, 'dept/neurology.html')


def opthomology(request):
    return render(request, 'dept/opthamology.html')


def paediatrics(request):
    return render(request, 'dept/paediatrics.html')


def ortho(request):
    return render(request, 'dept/orthopaedics.html')


def psy(request):
    return render(request, 'dept/psychiatry.html')


def pulmo(request):
    return render(request, 'dept/pulmonology.html')

# Create your views here.

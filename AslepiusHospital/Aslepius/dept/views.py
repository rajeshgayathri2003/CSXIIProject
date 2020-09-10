from django.shortcuts import render
from dept.models import Departments

def dept(request):
    return render(request, 'dept/departments.html')


def gynaecology(request):
    obj=Departments.objects.get(doctorID=1)
    obj1=Departments.objects.get(doctorID=2)
    obj2=Departments.objects.get(doctorID=3)
    context={
        'object':obj,
        'object1':obj1,
        'object2':obj2
    }
    return render(request,'dept/gynaecology1.html',context)

def paediatrics(request):
    obj=Departments.objects.get(doctorID=4)
    obj1=Departments.objects.get(doctorID=5)
    obj2=Departments.objects.get(doctorID=6)
    obj3=Departments.objects.get(doctorID=7)
    context={
        'object':obj,
        'object1':obj1,
        'object2':obj2,
        'object3':obj3
    }
    return render(request,'dept/paediatrics1.html',context)

def nephrology(request):
    obj=Departments.objects.get(doctorID=8)
    obj1=Departments.objects.get(doctorID=9)
    obj2=Departments.objects.get(doctorID=10)
    context={
        'object':obj,
        'object1':obj1,
        'object2':obj2
    }
    return render(request,'dept/nephrology1.html',context)

def neurology(request):
    obj=Departments.objects.get(doctorID=11)
    obj1=Departments.objects.get(doctorID=12)
    obj2=Departments.objects.get(doctorID=13)
    context={
        'object':obj,
        'object1':obj1,
        'object2':obj2
    }
    return render(request,'dept/neurology1.html',context)


def orthopaedics(request):
    obj=Departments.objects.get(doctorID=14)
    obj1=Departments.objects.get(doctorID=15)
    obj2=Departments.objects.get(doctorID=16)
    context={
        'object':obj,
        'object1':obj1,
        'object2':obj2
    }
    return render(request,'dept/orthopaedics1.html',context)


def dermatology(request):
    obj=Departments.objects.get(doctorID=17)
    context={
        'object':obj
    }
    return render(request,'dept/dermatology1.html',context)

def ENT(request):
    obj=Departments.objects.get(doctorID=18)
    obj1=Departments.objects.get(doctorID=19)
    obj2=Departments.objects.get(doctorID=20)
    context={
        'object':obj,
        'object1':obj1,
        'object2':obj2
    }
    return render(request,'dept/ENT1.html',context)

def dental(request):
    obj=Departments.objects.get(doctorID=21)
    obj1=Departments.objects.get(doctorID=22)
    context={
        'object':obj,
        'object1':obj1
    }
    return render(request,'dept/dental1.html',context)

def endocrinology(request):
    obj=Departments.objects.get(doctorID=23)
    obj1=Departments.objects.get(doctorID=24)
    obj2=Departments.objects.get(doctorID=25)
    context={
        'object':obj,
        'object1':obj1,
        'object2':obj2
    }
    return render(request,'dept/endocrinology1.html',context)


def General_Physicians(request):
    obj=Departments.objects.get(doctorID=26)
    obj1=Departments.objects.get(doctorID=27)
    obj2=Departments.objects.get(doctorID=28)
    obj3=Departments.objects.get(doctorID=29)
    obj4=Departments.objects.get(doctorID=30)
    context={
        'object':obj,
        'object1':obj1,
        'object2':obj2,
        'object3': obj3,
        'object4': obj4
    }
    return render(request,'dept/General_Physicians1.html',context)

def cardiology(request):
    obj=Departments.objects.get(doctorID=31)
    obj1=Departments.objects.get(doctorID=32)
    obj2=Departments.objects.get(doctorID=33)
    context={
        'object':obj,
        'object1':obj1,
        'object2':obj2
    }
    return render(request,'dept/cardiology1.html',context)

def pulmonology(request):
    obj=Departments.objects.get(doctorID=34)
    obj1=Departments.objects.get(doctorID=35)
    obj2=Departments.objects.get(doctorID=36)
    obj3=Departments.objects.get(doctorID=37)
    context={
        'object':obj,
        'object1':obj1,
        'object2':obj2,
        'object3': obj3,
    }
    return render(request,'dept/pulmonology1.html',context)

def psychiatry(request):
    obj=Departments.objects.get(doctorID=38)
    obj1=Departments.objects.get(doctorID=39)
    obj2=Departments.objects.get(doctorID=40)
    context={
        'object':obj,
        'object1':obj1,
        'object2':obj2
    }
    return render(request,'dept/psychiatry1.html',context)

def opthomology(request):
    obj=Departments.objects.get(doctorID=41)
    obj1=Departments.objects.get(doctorID=42)
    obj2=Departments.objects.get(doctorID=43)
    context={
        'object':obj,
        'object1':obj1,
        'object2':obj2
    }
    return render(request,'dept/opthamology1.html',context)

def diet_and_nutrition(request):
    obj=Departments.objects.get(doctorID=44)
    obj1=Departments.objects.get(doctorID=45)
    context={
        'object':obj,
        'object1':obj1
    }
    return render(request,'dept/diet_and_nutrition1.html',context)


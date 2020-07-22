from django.shortcuts import render

def vaccines(request):
    return render(request,'vaccines/Vaccines.html')

def birth(request):
    return render(request, 'vaccines/Birth.html')

def two_Months(request):
    return render(request,'vaccines/2Months.html')



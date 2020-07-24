from django.shortcuts import render


def FrontScreen(request):
    return render(request, 'opening/opening.html')

def covid(request):
    return render(request, 'opening/Covid19.html')

def BabyBlue(request):
    return render(request, 'opening/BlueBabySyndrome.html')

def Brain_Tumour(request):
    return render(request, 'opening/Brain_Tumour.html')

def heart(request):
    return render(request, 'opening/HeartHealth.html')


def KidneyCare(request):
    return render(request,'opening/KidneyCancer.html')

def KidneyPain(request):
    return render(request, 'opening/KidneyPain.html')

def faq(request):
    return render(request,'faq/faq.html')

def aboutus(request):
    return render(request,'opening/about.html')
# Create your views here.

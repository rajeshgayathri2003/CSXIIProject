from django.shortcuts import render

def bookappointment(request):
    return render (request, 'appointment/bookapt.html')

# Create your views here.

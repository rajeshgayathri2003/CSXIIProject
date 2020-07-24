from django.shortcuts import render
import csv
from datetime import datetime


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
        return render(request, 'contactus/thankyou.html')
    else:
        return render(request, 'contactus/contact.html')

def contactthankyou(request):
    return render(request,'contactus/thankyou.html')
# Create your views here.

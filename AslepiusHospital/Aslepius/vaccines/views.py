from django.shortcuts import render
from vaccines.models import Vaccines, Availability, Vaccines_payment
from dept import views as deptviews
from dept.models import Departments
from django.core.mail import send_mail
from login import models as loginmodels
from appointment import models as aptmodels
from django.contrib import messages
from labs import models as labs

def vaccines(request):
    return render(request,'vaccines/Vaccines.html')

# def birth(request):
#     return render(request, 'vaccines/Birth.html')

# def two_Months(request):
#     return render(request,'vaccines/2Months.html')

# def four_Months(request):
#     return render(request,'vaccines/4Months.html')

# def six_Months(request):
#     return render(request,'vaccines/6Months.html')

# def nine_twelve_Months(request):
#     return render(request,'vaccines/9-12Months.html')

# def fifteen_eighteen_Months(request):
#     return render(request,'vaccines/15-18Months.html')

# def two_three_Years(request):
#     return render(request,'vaccines/2-3Years.html')

# def five_Years(request):
#     return render(request,'vaccines/5Years.html')

# def seven_seventeen_Years(request):
#     return render(request,'vaccines/7-17Years.html')


def birth(request):
    obj = Vaccines.objects.get(VaccineID = 'HPBB')
    obj1 = Vaccines.objects.get(VaccineID = 'BCGB')
    obj2 = Vaccines.objects.get(VaccineID = 'OPVBR')
    context = {
        'object': obj,
        'object1': obj1,
        'object2': obj2
    }
    return render(request, 'vaccines/Birth1.html', context)

def two_Months(request):
    obj = Vaccines.objects.get(VaccineID = 'RTV1')
    obj1 = Vaccines.objects.get(VaccineID = 'HIB1')
    obj2 = Vaccines.objects.get(VaccineID = 'OPV1')
    obj3 = Vaccines.objects.get(VaccineID = 'DTP1')
    obj4 = Vaccines.objects.get(VaccineID = 'HPB2')
    context = {
        'object': obj,
        'object1': obj1,
        'object2': obj2,
        'object3': obj3,
        'object4': obj4
    }
    return render(request, 'vaccines/2Months1.html', context)

def four_Months(request):
    obj = Vaccines.objects.get(VaccineID = 'HIB2')
    obj1 = Vaccines.objects.get(VaccineID = 'RTV2')
    obj2 = Vaccines.objects.get(VaccineID = 'DTP2')
    obj3 = Vaccines.objects.get(VaccineID = 'OPV2')
    context = {
        'object': obj,
        'object1': obj1,
        'object2': obj2,
        'object3': obj3
    }  
    return render(request, 'vaccines/4Months1.html', context)

def six_Months(request):
    obj = Vaccines.objects.get(VaccineID = 'HPB3')
    obj1 = Vaccines.objects.get(VaccineID = 'DTP3')
    obj2 = Vaccines.objects.get(VaccineID = 'RTV3')
    obj3 = Vaccines.objects.get(VaccineID = 'HIB3')
    obj4 = Vaccines.objects.get(VaccineID = 'OPV3')
    context = {
        'object': obj,
        'object1': obj1,
        'object2': obj2,
        'object3': obj3,
        'object4' : obj4
    }  
    return render(request, 'vaccines/6Months1.html', context)

def nine_twelve_Months(request):
    obj = Vaccines.objects.get(VaccineID = 'MMR1')
    obj1 = Vaccines.objects.get(VaccineID = 'HPA1')
    obj2 = Vaccines.objects.get(VaccineID = 'HIB4')
    context = {
        'object': obj,
        'object1': obj1,
        'object2': obj2
    }  
    return render(request, 'vaccines/9-12Months1.html', context)

def fifteen_eighteen_Months(request):
    obj = Vaccines.objects.get(VaccineID = 'VRC1')
    obj1 = Vaccines.objects.get(VaccineID = 'DTP4')
    obj2 = Vaccines.objects.get(VaccineID = 'HPA2')
    obj3 = Vaccines.objects.get(VaccineID = 'OPVB1')
    obj4 = Vaccines.objects.get(VaccineID = 'MMR2')
    context = {
        'object': obj,
        'object1': obj1,
        'object2': obj2,
        'object3': obj3,
        'object4': obj4
    }  
    return render(request, 'vaccines/15-18Months1.html', context)

def two_three_Years(request):
    obj = Vaccines.objects.get(VaccineID = 'TY1')
    obj1 = Vaccines.objects.get(VaccineID = 'TYB')
    context = {
        'object': obj,
        'object1': obj1
    }  
    return render(request, 'vaccines/2-3Years1.html', context)

def five_Years(request):
    obj = Vaccines.objects.get(VaccineID = 'OPVB2')
    obj1 = Vaccines.objects.get(VaccineID = 'VRCB')
    obj2 = Vaccines.objects.get(VaccineID = 'MMRB1')
    obj3 = Vaccines.objects.get(VaccineID = 'DTP5')
    context = {
        'object': obj,
        'object1': obj1,
        'object2': obj2,
        'object3': obj3
    }  
    return render(request, 'vaccines/5Years1.html', context)

def seven_seventeen_Years(request):
    obj = Vaccines.objects.get(VaccineID = 'TD1')
    obj1 = Vaccines.objects.get(VaccineID = 'HPVC')
    obj2 = Vaccines.objects.get(VaccineID = 'HPVG')
    obj3 = Vaccines.objects.get(VaccineID = 'MMRB2')
    obj4 = Vaccines.objects.get(VaccineID = 'TDB')
    context = {
        'object': obj,
        'object1': obj1,
        'object2': obj2,
        'object3': obj3,
        'object4': obj4
    }  
    return render(request, 'vaccines/7-17Years1.html', context)

# def get_chkbox_value(request):


def book_appointment(request):
    return render(request, 'vaccines/bookapt.html')

def ThankYou(request):
    return render(request,'vaccines/ThankYou.html')

def Home(request):
    return render(request, 'mypage/myhomepage.html')

def get_chkbox_value(request):
    if request.method == "POST":
        vaccine = request.POST['vaccine']
        print(vaccine)
        if vaccine == 'HPBB':
            vaccine = Vaccines.objects.filter(VaccineID="HPBB")
            return render(request, 'vaccines/payments.html', {'v_lst': vaccine})
        elif vaccine == 'BCGB':
            vaccine = Vaccines.objects.filter(VaccineID="BCGB")
            return render(request, 'vaccines/payments.html', {'v_lst': vaccine})
        elif vaccine == 'OPVBR':
            vaccine = Vaccines.objects.filter(VaccineID="OPVBR")
            return render(request, 'vaccines/payments.html', {'v_lst': vaccine})
        elif vaccine == 'RTV1':
            vaccine = Vaccines.objects.filter(VaccineID="RTV1")
            return render(request, 'vaccines/payments.html', {'v_lst': vaccine})
        elif vaccine == 'HIB1':
            vaccine = Vaccines.objects.filter(VaccineID="HIB1")
            return render(request, 'vaccines/payments.html', {'v_lst': vaccine})
        elif vaccine == 'OPV1':
            vaccine = Vaccines.objects.filter(VaccineID="OPV1")
            return render(request, 'vaccines/payments.html', {'v_lst': vaccine})
        elif vaccine == 'DTP1':
            vaccine = Vaccines.objects.filter(VaccineID="DTP1")
            return render(request, 'vaccines/payments.html', {'v_lst': vaccine})
        elif vaccine == 'HPB2':
            vaccine = Vaccines.objects.filter(VaccineID="HPB2")
            return render(request, 'vaccines/payments.html', {'v_lst': vaccine})
        elif vaccine == 'HIB2':
            vaccine = Vaccines.objects.filter(VaccineID="HIB2")
            return render(request, 'vaccines/payments.html', {'v_lst': vaccine})
        elif vaccine == 'RTV2':
            vaccine = Vaccines.objects.filter(VaccineID="RTV2")
            return render(request, 'vaccines/payments.html', {'v_lst': vaccine})
        elif vaccine == 'DTP2':
            vaccine = Vaccines.objects.filter(VaccineID="DTP2")
            return render(request, 'vaccines/payments.html', {'v_lst': vaccine})
        elif vaccine == 'OPV2':
            vaccine = Vaccines.objects.filter(VaccineID="OPV2")
            return render(request, 'vaccines/payments.html', {'v_lst': vaccine})
        elif vaccine == 'HPB3':
            vaccine = Vaccines.objects.filter(VaccineID="HPB3")
            return render(request, 'vaccines/payments.html', {'v_lst': vaccine})
        elif vaccine == 'DTP3':
            vaccine = Vaccines.objects.filter(VaccineID="DTP3")
            return render(request, 'vaccines/payments.html', {'v_lst': vaccine})
        elif vaccine == 'RTV3':
            vaccine = Vaccines.objects.filter(VaccineID="RTV3")
            return render(request, 'vaccines/payments.html', {'v_lst': vaccine})
        elif vaccine == 'HIB3':
            vaccine = Vaccines.objects.filter(VaccineID="HIB3")
            return render(request, 'vaccines/payments.html', {'v_lst': vaccine})
        elif vaccine == 'OPV3':
            vaccine = Vaccines.objects.filter(VaccineID="OPV3")
            return render(request, 'vaccines/payments.html', {'v_lst': vaccine})
        elif vaccine == 'MMR1':
            vaccine = Vaccines.objects.filter(VaccineID="MMR1")
            return render(request, 'vaccines/payments.html', {'v_lst': vaccine})
        elif vaccine == 'HPA1':
            vaccine = Vaccines.objects.filter(VaccineID="HPA1")
            return render(request, 'vaccines/payments.html', {'v_lst': vaccine})
        elif vaccine == 'HIB4':
            vaccine = Vaccines.objects.filter(VaccineID="HIB4")
            return render(request, 'vaccines/payments.html', {'v_lst': vaccine})
        elif vaccine == 'VRC1':
            vaccine = Vaccines.objects.filter(VaccineID="VRC1")
            return render(request, 'vaccines/payments.html', {'v_lst': vaccine})
        elif vaccine == 'DTP4':
            vaccine = Vaccines.objects.filter(VaccineID="DTP4")
            return render(request, 'vaccines/payments.html', {'v_lst': vaccine})
        elif vaccine == 'HPA2':
            vaccine = Vaccines.objects.filter(VaccineID="HPA2")
            return render(request, 'vaccines/payments.html', {'v_lst': vaccine})
        elif vaccine == 'OPVB1':
            vaccine = Vaccines.objects.filter(VaccineID="OPVB1")
            return render(request, 'vaccines/payments.html', {'v_lst': vaccine})
        elif vaccine == 'MMR2':
            vaccine = Vaccines.objects.filter(VaccineID="MMR2")
            return render(request, 'vaccines/payments.html', {'v_lst': vaccine})
        elif vaccine == 'TY1':
            vaccine = Vaccines.objects.filter(VaccineID="TY1")
            return render(request, 'vaccines/payments.html', {'v_lst': vaccine})
        elif vaccine == 'TYB':
            vaccine = Vaccines.objects.filter(VaccineID="TYB")
            return render(request, 'vaccines/payments.html', {'v_lst': vaccine})
        elif vaccine == 'OPVB2':
            vaccine = Vaccines.objects.filter(VaccineID="OPVB2")
            return render(request, 'vaccines/payments.html', {'v_lst': vaccine})
        elif vaccine == 'VRCB':
            vaccine = Vaccines.objects.filter(VaccineID="VRCB")
            return render(request, 'vaccines/payments.html', {'v_lst': vaccine})
        elif vaccine == 'MMRB1':
            vaccine = Vaccines.objects.filter(VaccineID="MMRB1")
            return render(request, 'vaccines/payments.html', {'v_lst': vaccine})
        elif vaccine == 'DTP5':
            vaccine = Vaccines.objects.filter(VaccineID="DTP5")
            return render(request, 'vaccines/payments.html', {'v_lst': vaccine})
        elif vaccine == 'TD1':
            vaccine = Vaccines.objects.filter(VaccineID="TD1")
            return render(request, 'vaccines/payments.html', {'v_lst': vaccine})
        elif vaccine == 'HPVC':
            vaccine = Vaccines.objects.filter(VaccineID="HPVC")
            return render(request, 'vaccines/payments.html', {'v_lst': vaccine})
        elif vaccine == 'HPVG':
            vaccine = Vaccines.objects.filter(VaccineID="HPVG")
            return render(request, 'vaccines/payments.html', {'v_lst': vaccine})
        elif vaccine == 'MMRB2':
            vaccine = Vaccines.objects.filter(VaccineID="MMRB2")
            return render(request, 'vaccines/payments.html', {'v_lst': vaccine})
        elif vaccine == 'TDB':
            vaccine = Vaccines.objects.filter(VaccineID="TDB")
            return render(request, 'vaccines/payments.html', {'v_lst': vaccine})



def Payment(request):
    if request.method == "POST":
        fname = request.POST['firstname']
        email = request.POST['email']
        add = request.POST['address']
        city = request.POST['city']
        Vaccinename = request.POST.get('Vaccinename')
        price = request.POST['price']
        state = request.POST['state']
        pincode = request.POST['Pincode']
        cardname = request.POST['cardname']
        creditcard_num = request.POST['cardnumber']
        expiry_month = request.POST['expmonth']
        expiry_year = request.POST['expyear']
        cvv = request.POST['cvv']
        R = Vaccines_payment()
        R.patientID = request.user
        R.fname=fname
        R.Add=add
        R.city=city
        R.Vaccinename=Vaccinename
        R.price=price
        R.state=state
        R.pincode=pincode
        R.cardname=cardname
        R.cardnumber=creditcard_num
        R.exp_month=expiry_month
        R.exp_year=expiry_year
        R.cvv= cvv
        R.save()
        body = 'Dear {0},\nYour appointment for the {1} vaccine has been confirmed \n Please be on time.\n Regards,\nTeam Aselpius'.format(fname, Vaccinename )
        send_mail('Appointment Confirmation', body,
                  'aslepius9@gmail.com', [request.user.email, ], fail_silently=False)
        details_lst = loginmodels.Register.objects.filter(email=request.user.id)
        appointment_lst = aptmodels.Appointment.objects.filter(status=0, patientID=request.user.id, )
        labs_lst = labs.Labs_payment.objects.filter(patientID=request.user.id)
        vaccines_lst = Vaccines_payment.objects.filter(patientID=request.user.id, )
        return render(request, 'vaccines/ThankYou.html',{'d_lst': details_lst, 'a_lst': appointment_lst, 'l_lst': labs_lst, 'v_lst': vaccines_lst})


def Vaccine_confirm(request):
    if request.method == "POST":
        bookingID = request.POST.get('bookingID')
        print('1',bookingID)
        obj_delete = Vaccines_payment.objects.filter(bookingID= bookingID)
        l_dict = {'bookingID': obj_delete}
        print(l_dict)
    return render(request, 'vaccines/confirmcancel.html', l_dict)

'''This function enables the patient to cancel the appointment'''
def Vaccine_cancel(request):
    if request.method == "POST":
        bookingID = request.POST.get('bookingID')
        obj_delete = Vaccines_payment.objects.get(bookingID= bookingID)
        obj_delete.delete()
        print("SUCCESS")
        return render(request, 'vaccines/cancelvaccine.html')
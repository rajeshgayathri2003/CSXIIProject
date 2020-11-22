from django.shortcuts import render, redirect
import csv
from datetime import datetime
from . import models
from random import randint
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.hashers import check_password
from appointment import models as aptmodels
from labs import models as labs
from dept import models as deptmodels


'''This function is used to generate a random password that will 
be sent to the user's email. The user will be asked to change this 
during his first login
'''
def generatepasswd():
    digit=str(randint(0,9))
    rannumu = randint(65,90)
    rannuml = randint(97,122)
    rannum2 = randint(97,122)
    rannumu1 = randint(65,90)
    Lspecchar=[",","<",">",".","?","/","\"","\'",":",";","[","]","{","]","\\","|","-","_","+","=","!","@","#","$","%","^","&","*","(",")"]
    rannumspec=randint(1,len(Lspecchar))
    ualpha=""
    lalpha=""
    specchar=""
    ualpha=chr(rannumu)
    lalpha=chr(rannuml)
    lalpha2 = chr(rannum2)
    ualpha2 = chr(rannumu1)
    specchar=Lspecchar[rannumspec]
    passwd = digit+ualpha+lalpha+specchar+lalpha2+ualpha2
    return passwd


'''This function enables the user to regsiter with
Aslepius Hospital. The user's email id and name is
written on to the Django's User Model. If the email
is already present in the database it returns a message
saying that the email already exists'''
key = None
mailkey = None
def login(request):
    global key
    global mailkey
    if request.method == "POST":
        username = request.POST['mail']
        email = request.POST['mail']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        mailkey = email
        if User.objects.filter(username=username).exists():
            messages.info(request,'Email already exists')
            return redirect('login')
        else:
            password = generatepasswd()
            user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name,
                                                   password=password)
            user.save();
            body = 'Welcome to Aslepius\nYour username is {0}\n Your Password is {1}\nRegards,\nTeam Aslepius'.format(mailkey,password)
            send_mail('Registration Successful',
             body,'aslepius9@gmail.com',
             [mailkey],
             fail_silently= False)
            P  =models.Temporary_passwd()
            P.email= email
            P.temppasswd = password
            P.save()
            return render(request,'login/loginthankyou.html')
    else:
        return render(request, 'login/login.html')


'''When the user logs in for the first time (s)he is asked 
to change the password and then enter details like address, gender,
and date of birth'''
def registration(request):
    if request.method == "GET":
        return render(request, 'login/registration.html',)
    else:
        '''name = request.POST['name']'''
        dob = request.POST['dob']
        gender = request.POST['Gender']
        if gender=='female':
            gender='F'
        elif gender=='Male':
            gender='M'
        elif gender=='Other':
            gender='O' 
        details_lst_1 = User.objects.get(email=mailkey)
        mobile = request.POST['mobile']
        Add1 = request.POST['Add1']
        Add2 = request.POST['Add2']
        Add3 = request.POST['Add3']
        city = request.POST['city']
        state = request.POST['state']
        pincode = request.POST['pincode']

        
        R = models.Register()
        R.dob = dob  #Issue sorted
        R.gender = gender # Issue Sorted
        R.email = details_lst_1
        R.mobile = mobile #Issue Sorted
        R.Add1 = Add1
        R.Add2 = Add2
        R.Add3 = Add3  # Issue sorted
        R.city = city
        R.state = state
        R.pincode = pincode
        R.save()
        messages.info(request, 'Kindly login with your new password')
        return redirect('login')    


'''This function authenticates the user and then
takes him to a personalised page, where his name, address,
email, DOB, appoitments he booked, the labs and test will 
be displayed'''
'''Khushi and Shraddha, you need to add the retrieve operation here
so that the user can see her test and vaccines related data here'''
def mypage(request):
    if request.method== "POST":
        email = request.POST['email']
        passwd = request.POST['password']
        print("#",passwd)
        print("#",models.Temporary_passwd.objects.get(email=email).temppasswd)
        user = auth.authenticate(username=email, password=passwd)
        if user is not None:
            auth.login(request, user)
            if passwd == models.Temporary_passwd.objects.get(email=email).temppasswd:
                return render(request,'login/changepassword.html')
            else:
                username = email
                details_lst = models.Register.objects.filter(email = request.user.id)
                appointment_lst = aptmodels.Appointment.objects.filter(patientID = request.user.id)
                labs_lst = labs.Labs_payment.objects.filter(patientID=request.user.id)
                returndict = {'d_lst': details_lst, 'a_lst': appointment_lst, 'l_lst':labs_lst}
                return render(request, 'mypage/myhomepage.html', returndict)

        else:
            messages.info(request,'Username or password is incorrect')
            return redirect('login')
    else:
        username = request.user.username
        details_lst = models.Register.objects.filter(email= request.user.id)
        appointment_lst = aptmodels.Appointment.objects.filter(status =0, patientID = request.user.id, )
        labs_lst = labs.Labs_payment.objects.filter(patientID=request.user.id,)
        return render(request,'mypage/myhomepage.html',{'d_lst': details_lst, 'a_lst': appointment_lst, 'l_lst': labs_lst})


'''Upon first login the User is asked to change her password. 
The above function performs this functionality'''
def updatepasswdlogin(request):
    if request.method == 'POST':
        username = request.user.username
        print(username)
        newpasswd = request.POST['newpasswd']
        newpasswdconfirm = request.POST['confirmnewpasswd']
        user_lst = User.objects.get(email=username)
        if newpasswdconfirm == newpasswd:
            user_lst.set_password(newpasswd)
            user_lst.save()
            return render(request,'login/registration.html')
        else:
            messages.info(request, "New passwords don't match")
            return redirect('updatepasswdlogin')
    else:
        return render(request,'login/changepassword.html')

'''This function enables the user to log out of the page'''
def logout(request):
    auth.logout(request)
    return redirect('/')

# Create your views here.

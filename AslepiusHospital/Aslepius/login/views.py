from django.shortcuts import render, redirect
import csv
from datetime import datetime
from . import models
from random import randint
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.hashers import check_password
import mysql.connector
con=mysql.connector.connect(host='localhost', user='root', passwd='G@Y@3rajesh', database='GAYATHRI')
mycursor= con.cursor()

def generatepasswd():
    digit=str(randint(0,9))
    rannumu=randint(65,90)
    rannuml=randint(97,122)
    Lspecchar=[",","<",">",".","?","/","\"","\'",":",";","[","]","{","]","\\","|","-","_","+","=","!","@","#","$","%","^","&","*","(",")"]
    rannumspec=randint(1,len(Lspecchar))
    ualpha=""
    lalpha=""
    specchar=""
    ualpha=chr(rannumu)
    lalpha=chr(rannuml)
    specchar=Lspecchar[rannumspec]
    passwd = digit+ualpha+lalpha+specchar
    return passwd


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
        # password = request.POST['passwd']
        # key = password
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
            return render(request,'login/loginthankyou.html')
            # user_list = User.objects.filter(email=email)
            # print(user_list)
            '''for i in user_list:
            key = i.id'''
            # return render(request,'login/loginthankyou.html',{'user_list':user_list})

    else:
        return render(request, 'login/login.html')



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
            gender='O'  #Please check and make the necessary corrections
        '''if request.POST['female']=="on":
            gender="F"
        elif request.POST['Male']=="on":
            gender="M"
        elif request.POST['Other']=="on":
            gender="O"
        if 'female' in request.POST:
            gender = "F"
        elif 'Male' in request.POST:
            gender = "M"
        elif 'Other' in request.POST:
            gender = "O"'''
        '''email = request.POST['email']
        print(email)'''
        '''passwd = request.POST['passwd']'''
        lst = User.objects.filter(username= mailkey)
        for i in lst:
            print('hi',i)

        # confirmpasswd = request.POST['confirmpasswd']
        mobile = request.POST['mobile']
        Add1 = request.POST['Add1']
        Add2 = request.POST['Add2']
        Add3 = request.POST['Add3']
        city = request.POST['city']
        state = request.POST['state']
        pincode = request.POST['pincode']

        
        R = models.Register()
        R.patientid = randint(1000,9999)
        '''R.name = name'''
        R.dob = dob  #Issue sorted
        R.gender = gender #Minor bug- Allows multiple choices
        R.email = mailkey
        '''R.passwd = passwd'''
        # R.confirmpasswd = confirmpasswd
        #Issue Sorted
        R.mobile = mobile
        #Issue Sorted
        R.Add1 = Add1
        R.Add2 = Add2
        R.Add3 = Add3
        # Issue sorted
        R.city = city
        R.state = state
        R.pincode = pincode
        R.save()
        details_lst = models.Register.objects.filter(email=mailkey)
        return render(request, 'mypage/myhomepage.html', {'d_lst': details_lst})    


def mypage(request):
    if request.method== "POST":
        email = request.POST['email']
        passwd = request.POST['password']
        sql= "SELECT last_login from auth_user where email='{}';".format(email)
        mycursor.execute(sql)
        result = mycursor.fetchall()
        val=None
        for i in result:
            for j in i:
                val=j
        user = auth.authenticate(username=email, password=passwd)
        if user is not None:
            username = email
            details_lst = models.Register.objects.filter(email=username)
            print(details_lst)
            
            # obj=models.Register.objects.get(email=email)
            
            print(val)
            print(type(val))
            if val == "NULL":
                auth.login(request, user)
                return render('login/changepassword.html')
            else:
                auth.login(request, user)
                return render(request, 'mypage/myhomepage.html', {'d_lst': details_lst})
        else:
            messages.info(request,'Username or password is incorrect')
            return redirect('login')
    else:
        username = request.user.username
        details_lst = models.Register.objects.filter(email=username)
        return render(request,'mypage/myhomepage.html',{'d_lst': details_lst})

def updatepasswd(request):
    #if request.user.is_authenticated() why do I get an error?
    if request.method == 'POST':
        username = request.user.username
        # oldpasswd = request.POST['oldpasswd']
        newpasswd = request.POST['newpasswd']
        newpasswdconfirm = request.POST['newpasswdconfirm']
        #print(username)
        user_lst = User.objects.get(username=username)
        #print(user_lst)
        #print(user_lst.password)
        if newpasswdconfirm == newpasswd:
            #User.objects.filter(username=username).update(password=newpasswd)
            user_lst.set_password(newpasswd)
            user_lst.save()
            #print("Hello")
            messages.info(request, 'Update Successful')
            return render('login/registration.html')
        else:
            messages.info(request, "New passwords don't match")
            return redirect('updatepasswd')
    else:
        return render(request,'login/changepassword.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
'''
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
    return render(request, 'login/pulmonology.html')'''

'''def vaccines(request):
    return render(request,'login/vaccines.html')'''

'''def covid(request):
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
    return render(request, 'login/KidneyPain.html')'''

'''def contactthankyou(request):
    return render(request,'login/thankyou.html')'''

'''def FrontScreen(request):
    return render(request, 'login/opening.html')'''

'''def dept(request):
    return render(request, 'login/departments.html')


def cardiology(request):
    return render(request, 'login/cardiology.html')'''


'''def contact(request):
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
        return render(request, 'login/contact.html')'''

# Create your views here.

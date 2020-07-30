from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from login import models as loginmodels
def updatepasswd(request):
    #if request.user.is_authenticated() why do I get an error?
    if request.method == 'POST':
        username = request.user.username
        oldpasswd = request.POST['oldpasswd']
        newpasswd = request.POST['newpasswd']
        newpasswdconfirm = request.POST['newpasswdconfirm']
        #print(username)
        user_lst = User.objects.get(username=username)
        #print(user_lst)
        #print(user_lst.password)
        if check_password(oldpasswd, user_lst.password):
            '''print("OK")'''
            if newpasswdconfirm == newpasswd:
                #User.objects.filter(username=username).update(password=newpasswd)
                user_lst.set_password(newpasswd)
                user_lst.save()
                #print("Hello")
                messages.info(request, 'Update Successful')
                return redirect('updatepasswd')
            else:
                messages.info(request, "New passwords don't match")
                return redirect('updatepasswd')
        else:
            messages.info(request,"Old password doesn't match records")
            return redirect('updatepasswd')

    else:
        return render(request, 'mypage/updatepasswd.html')

def updateprofile(request):
    username=request.user.username
    if request.method=="POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        dob = request.POST['dob']
        mobile = request.POST['mobile']
        Add1 = request.POST['Add1']
        Add2 = request.POST['Add2']
        Add3 = request.POST['Add3']
        city = request.POST['city']
        state = request.POST['state']
        pincode = request.POST['pincode']
        user_lst= User.objects.filter(username=username)
        user_lst.update(first_name=fname, last_name=lname, username=email, email=email)
        details_lst = loginmodels.Register.objects.filter(email=username)
        details_lst.update(dob=dob, mobile=mobile, Add1=Add1, Add2= Add2, Add3=Add3, city=city, state=state, pincode=pincode)
        messages.info(request,'Update Successful')
        return redirect('updateprofile')
    else:
        details_lst= loginmodels.Register.objects.filter(email=username)
        print(details_lst)
        dob= loginmodels.Register.objects.get(email=username).dob.strftime('%y-%m-%d')
        print(dob)
        return render(request,'mypage/profilepage.html',{'d_lst':details_lst})

# Create your views here.

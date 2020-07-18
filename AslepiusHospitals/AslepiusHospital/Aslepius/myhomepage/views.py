from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.hashers import check_password
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


# Create your views here.

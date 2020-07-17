from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login , logout

def home(request):
    return render(request, 'todo/home.html')
def signupuser(request):
    if request.method =='GET':
        return render(request, 'todo/signupuser.html',{'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodos')

            except IntegrityError:
                return render(request,'todo/signupuser.html',{'form':UserCreationForm(),'error':'This username is not available anymore. Please use another name'})
        else:
            return render(request, 'todo/signupuser.html',{'form':UserCreationForm(),'error':'Passwords did not match'})
                        #Tell the user the passwords didn't match


def logoutuser(request):
    if request.method=='POST':
        logout(request)
        return redirect('home')
    else:
        return redirect('currenttodos')
def currenttodos(request):
    return render(request,'todo/currenttodos.html')

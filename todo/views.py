from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def signupuser(request):
    if request.method =='GET':
        return render(request, 'todo/signupuser.html',{'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            User.objects.create_user(request.POST['username'],password=request.POST['password1'])
            user.save()
        else:
            print("hi")
                        #Tell the user the passwords didn't match

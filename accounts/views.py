from django.shortcuts import render, redirect # type: ignore
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages

# Create your views here.

def register(request):
    if(request.method == 'POST'):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if(password1 == password2):
            if(User.objects.filter(username=username).exists()):
                messages.info(request, "UserName Taken")
                return redirect('register')
            elif(User.objects.filter(email=email).exists()):
                messages.info(request, "Email Taken")
                return redirect('register')
            else:
                user= User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request, "Registered User Successfully!!")
                return redirect('auth_login')
        else:
            messages.info(request, "Password not matching..")
            return redirect('register')
        return redirect('/')
    else:
        return render(request, "register.html")
    
def auth_login(request):
    if(request.method == "POST"):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if(user is None):
               messages.info(request, "Invalid Credentials!!")
               return redirect("auth_login")
        else:
            login(request, user)
            return redirect("/")
    else:
        return render(request, "login.html")

def auth_logout(request):
    logout(request)
    return redirect("/")
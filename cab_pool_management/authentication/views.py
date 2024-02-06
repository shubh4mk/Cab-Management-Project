from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout

# Create your views here.


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if not User.objects.filter(username=username).exists():
            if pass1==pass2:
                myuser = User.objects.create_user(username, email, pass1)
                myuser.first_name = fname
                myuser.last_name = lname
                myuser.save()
                return render(request,"authentication/signin.html",{'success_message': "User got Created"})
            else:
                return render(request,"authentication/signup.html",{'password_error_message': "Check your conformation password"})
        else:
            return render(request,"authentication/signup.html",{'username_error_message': "Username Already Exist"})
          
    return render(request, "authentication/signup.html")


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']
        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            return redirect('userindex')
            
        else:
            return render(request,"authentication/signin.html",{'error_message': "Check your Credentials"})

    return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    return redirect('signin')
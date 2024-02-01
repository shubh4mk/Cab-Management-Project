from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout

# Create your views here.

def userIndex(request):
    if request.user:
        user_id=request.user.id
        userObj=User.objects.get(id=user_id)
        return render(request, "user_dashboard/userIndex.html",{'user':userObj})

def signout(request):
    return redirect('signout')

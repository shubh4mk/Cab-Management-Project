from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def userIndex(request):
    user_id=request.user.id
    userObj=User.objects.get(id=user_id)
    return render(request, "user_dashboard/userIndex.html",{'user':userObj})

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path('userindex',views.userIndex,name='userindex'),
    path('account/',include('authentication.urls')),
]
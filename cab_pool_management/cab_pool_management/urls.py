"""
URL configuration for cab_pool_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from homepage.views import homepage,aboutus
from authentication.views import signin,signout,signup
from user_dashboard.views import userIndex
from cab_booking.views import booking


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage,name="homepage"),
    path('aboutUs',aboutus,name="aboutus"),
    path('signup', signup, name="signup"),
    path('signin', signin, name="signin"),
    path('signout',signout, name="signout"),
    path('userindex',userIndex,name='userindex'),
    path('bookcab',booking,name="bookcab")
]
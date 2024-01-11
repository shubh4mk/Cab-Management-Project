from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,"homepage/index.html")

def aboutus (request):
    return render(request,"aboutUs/aboutUs.html")

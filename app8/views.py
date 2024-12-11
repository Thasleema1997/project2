from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    return render(request,"home.html")

def admin(request):
    if request.method=="POST":
        Name=request.POST["name1"]
        Email=request.POST["name4"]
        Username=request.POST["name8"]
        Password=request.POST["name9"]
        db=com(Name=Name,Email=Email,Username=Username,Password=Password)
        db.save()
        return HttpResponse("Data is saved")

    return render(request,"admin.html")

def employee(request):
    return render(request,"employee.html")

def manager(request):
    return render(request,"manager.html")

def adminlogin(request):
    return render(request,"loginadmin.html")

def managerlogin(request):
    return render(request,"loginmanager.html")

def employeelogin(request):
    return render(request,"loginemployee.html")


def commonlogin(request):
    return render(request,"commonlogin.html")

def weladm(request):
    return render(request,"welcomeadmin.html")

def welemp(request):
    return render(request,"welcomeemployee.html")

def welman(request):
    return render(request,"welcomemanager.html")






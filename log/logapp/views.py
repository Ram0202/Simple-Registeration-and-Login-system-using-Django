from django.core.checks import messages
from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from logapp import models
from logapp.models import User
from django.contrib import messages


def signup(request):
    msg="username already taken"
    
    if request.method=="POST":
        username=req.POST['username']
        phoneno=req.POST['phoneno']
        gender=req.POST['gender']
        email=req.POST['email']
        password=req.POST['password']
        if User.objects.filter(username=username):
            return render(req,"signup.html",{"ivalid":msg})       
        else:     
            User(username=username,phoneno=phoneno,gender=gender,email=email,password=password).save()
            return redirect('/login')
    return render(request,"signup.html")
    
    
def login(request):   
    red="INVALID ENTRY"
    
    if request.method=="POST":
        global username
        global felt
        username=request.POST['username']
        felt=username[0]
        
        password=request.POST['password']
        if User.objects.filter(username=username) and User.objects.filter(password=password):
            return redirect('/home')
        else:
            return render(request,"login.html",{"col":red})

    return render(request,"login.html")
    
    
def home(request):
    return render(request,"home.html")
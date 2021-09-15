from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def login(request):
    #default address and password
    username='jeng'
    password='1234'
    if request.method=="POST":
        if not 'username' in request.session:
            if request.POST['username']==username and request.POST['password']==password:
                request.session['username']=username
                message=username+"hello ,login success"
                status="login"
    else:
        if 'username' in request.session:
            if request.session['username']==username:
                message=request.session["username"]+"you have login"
                status="login"
    return render(request,'login.html',locals())
    
def logout(request):
    if 'username' in request.session:
        message=request.session['username']+"you have logout"
        del request.session['username']#delete session
    return render(request,'login.html',locals())


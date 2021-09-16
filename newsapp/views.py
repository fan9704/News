from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def login(request):
    #default address and password
    username='1'
    password='1'
    if request.method=="POST":
        if not 'username' in request.session:
            if request.POST['username']==username and request.POST['password']==password:
                request.session['username']=username
                message=username+" hello ,login success"
                status="login"
            else:
                message="密碼錯誤 或 使用者名稱不存在"
    else:
        if 'username' in request.session:
            if request.session['username']==username:
                message=request.session["username"]+" you have login"
                status="login"
    return render(request,'login.html',locals())
    
def logout(request):
    if 'username' in request.session:
        message=request.session['username']+" you have logout"
        del request.session['username']#delete session
    return render(request,'login.html',locals())

def index(request):
	if "counter" in request.COOKIES:
		counter=int(request.COOKIES["counter"])
		counter+=1
	else:		
		counter=1
	response = HttpResponse('今日瀏覽次數：' + str(counter))		
	tomorrow = datetime.datetime.now() + datetime.timedelta(days = 1)
	tomorrow = datetime.datetime.replace(tomorrow, hour=0, minute=0, second=0)
	expires = datetime.datetime.strftime(tomorrow, "%a, %d-%b-%Y %H:%M:%S GMT") 
	response.set_cookie("counter",counter,expires=expires)
	return response	

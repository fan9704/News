from django.shortcuts import render
from django.http import HttpResponse
from newsapp import models
import datetime
import math
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

def index(request,pageindex=None):
    page1=1 #store page1 value
    pagesize=8
    newsall=models.NewsUnit.objects.all().order_by('-id')#read datatable descending by id
    datasize=len(newsall)
    totpage=math.ceil(datasize/pagesize)
  
    if pageindex==None:
        page1=1
        newsunits=models.NewsUnit.objects.filter(enabled=True).order_by('-id')[:pagesize]
    elif pageindex=='1':#last page
        start=(page1-1 )*pagesize
        if start>=0:
            newsunits=models.NewsUnit.objects.filter(enabled=True).order_by('-id')[start:(start+pagesize)]
            page1-=1
    elif pageindex=='2':#next page
        start=(page1 )*pagesize
        if start<datasize:
            newsunits=models.NewsUnit.objects.filter(enabled=True).order_by('-id')[start:(start+pagesize)]
            page1+=1   
    elif pageindex=='3':
        # start=(page1 -1)*pagesize
        page1=1
        start=0
        if start>=0:
            newsunits=models.NewsUnit.objects.filter(enabled=True).order_by('-id')[start:(start+pagesize)]
    currentpage=page1
    print("totpage ",totpage,"currentpage ",currentpage)
    return render(request,"index.html",locals())


	# if "counter" in request.COOKIES:
	# 	counter=int(request.COOKIES["counter"])
	# 	counter+=1
	# else:		
	# 	counter=1
	# response = HttpResponse('今日瀏覽次數：' + str(counter))		
	# tomorrow = datetime.datetime.now() + datetime.timedelta(days = 1)
	# tomorrow = datetime.datetime.replace(tomorrow, hour=0, minute=0, second=0)
	# expires = datetime.datetime.strftime(tomorrow, "%a, %d-%b-%Y %H:%M:%S GMT") 
	# response.set_cookie("counter",counter,expires=expires)
	# return response	

def detail(request,detailid=None):
    unit=models.NewsUnit.objects.get(id=detailid)
    category=unit.catego
    title=unit.title
    pubtime=unit.pubtime
    nickname=unit.nickname
    message=unit.message
    unit.press+=1
    unit.save()

    return render(request,'detail.html',locals())
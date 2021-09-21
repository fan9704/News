from django.shortcuts import redirect, render
from django.http import HttpResponse
from newsapp import models
import datetime
import math
from django.contrib.auth import authenticate
from django.contrib import auth 
# Create your views here.


def login(request):
    messages=''
    if request.method=='POST':
        name=request.POST['username'].strip()
        password=request.POST['password']
        user1=authenticate(username=name,password=password)
        if user1 is not None:# pass authenticate
            if user1.is_active:
                auth.login(request,user1)
                return redirect('/adminmain/')
            else:
                messages="帳號未啟用"
        else:
            messages='登入失敗'
    return render(request,'login.html',locals())     
def logout(request):
    auth.logout(request)
    return redirect('/index/')
def login2(request):   
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
    return render(request,'login2.html',locals())
    
def logout2(request):
    if 'username' in request.session:
        message=request.session['username']+" you have logout"
        del request.session['username']#delete session
    return render(request,'login2.html',locals())

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

def newsadd(request):
    message=''
    category=request.POST.get('news_type','')
    subject=request.POST.get('news_subject','')
    editor=request.POST.get('news_editor','')
    content=request.POST.get('news_content','')
    ok=request.POST.get('news_ok','')
    if subject=='' or editor=='' or content=='':
        message='每個欄位都需要填寫'
    else:
        if ok=='yes':
            enabled=True
        else:
            enabled=False
        unit=models.NewsUnit.objects.create(catego=category,nickname=editor,title=subject,message=content,enabled=enabled,press=0)
        unit.save()
        return redirect('/adminmain/')
    return render(request,'newsadd.html',locals())


def adminmain(request, pageindex=None):  #管理頁面
	page1=0
	pagesize = 8
	newsall = models.NewsUnit.objects.all().order_by('-id')
	datasize = len(newsall)
	totpage = math.ceil(datasize / pagesize)
	if pageindex==None:
		page1 = 1
		newsunits = models.NewsUnit.objects.order_by('-id')[:pagesize]
	elif pageindex=='1':
		start = (page1)*pagesize
		if start >= 0:
			newsunits = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
			page1 -= 1
	elif pageindex=='2':
		start = (page1+1)*pagesize
		if start < datasize:
			newsunits = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
			page1 += 1
	elif pageindex=='3':
		start = (page1-1)*pagesize
		newsunits = models.NewsUnit.objects.order_by('-id')[start:(start+pagesize)]
	currentpage = page1
	return render(request, "adminmain.html", locals())

def newsedit(request,newsid=None,edittype=None):
    unit=models.NewsUnit.objects.get(id=newsid)
    categories=["公告",'更新','活動','其他']
    if edittype ==None:
        type=unit.catego
        subject=unit.title
        editor=unit.nickname
        content=unit.message
        ok=unit.enabled
    elif edittype=='1':
        category=request.POST.get('news_type','')
        subject=request.POST.get('news_subject','')
        editor=request.POST.get('news_editor','')
        content=request.POST.get('news_content','')
        ok=request.POST.get('news_ok','')
        if ok=='yes':
            enabled=True
        else:
            enabled=False
            unit.catego=category
            unit.nickname=editor
            unit.title=subject
            unit.message=content
            unit.enabled=enabled
            unit.save()
            return redirect('/adminmain/')
    
    return render(request,'newsedit.html',locals())

def newsdelete(request,newsid=None,deletetype=None):
    unit=models.NewsUnit.objects.get(id=newsid)
    if deletetype==None:
        type=str(unit.catego.category.strip())
        subject=unit.title
        editor=unit.nickname
        content=unit.message
        date=unit.pubtime
    elif deletetype =='1':
        unit.delete()
        return redirect('/adminmain/')
    return render(request,'newsdelete.html',locals())
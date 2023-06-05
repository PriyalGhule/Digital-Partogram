from django.template import loader
from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import Details
from .models import Parto_dets
from .utils import get_plot
from .utils import get_plot1
from .models import Section1
from .models import Section2
from .models import Section3
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def signup(request):
    if request.method=="POST":
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        password=request.POST.get("password")
        role=request.POST.get("role")
        print(email, phone, password, role)
        obj=Details()
        obj.email=email
        obj.role=role
        obj.password=password
        obj.phone=phone
        obj.save()
        detail=Details.objects.all()
        #return redirect(request,"registration/login.html")
        User.objects.create_user(email=email, password=password,username=email)
        for i in detail:
            print(email)
    return render(request,"registration/signup.html")


def login(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        user=authenticate(email=email, password=password)

        if user is not None:
            login(request, user)
            #fname=user.fname
            return redirect("Partogram_dets") 
        else:
            return redirect("Partogram_dets")
    return render(request,"registration/login.html")

def home(request):
    return HttpResponse(request,"Incorrect login details")

def Partogram_dets(request):
    if request.method =="POST":
        cerv_dil=request.POST.get("cerv_dil")
        hour=request.POST.get("hour")
        time=request.POST.get("time")
        obj1=Parto_dets()
        obj1.c_dilation=cerv_dil
        obj1.hours=hour
        obj1.time=time
        obj1.save()
      
    
    hr=[]
    cerv=[]
    pdets=Parto_dets.objects.values_list('hours') 
    pdetscerv=Parto_dets.objects.values_list('c_dilation')  
    for i in pdets:
        for j in i:
            #print(j)
            hr.append(j)
            print("hr",hr)
    x1=[0,1,2,3,4,5,6]
    y1=[4,5,6,7,8,9,10]
    x2=[4,5,6,7,8,9,10]
    y2=[4,5,6,7,8,9,10]
    for i in pdetscerv:
        for j in i:
            #print(j)
            cerv.append(j)
            print("cerv",cerv)

    template = loader.get_template('graph/graph.html')
    
    chart=get_plot(hr,cerv,x1,y1,x2,y2)
    context={'chart':chart, 'pdets':pdets}
    print(pdets)
    for i in pdets:
        for j in i:
            print(j ,end=" ")
    return HttpResponse(template.render(context, request))   
    #return render(request, "graph/graph.html",context)


def Section1_view(request):
    if request.method=="POST":
        fhr=request.POST.get("fhrh")
        hrs=request.POST.get("hrsh")
        sec=Section1()
        sec.fhr=fhr
        sec.hrs=hrs
        sec.save()

    fhrl=[]
    hrsl=[]
    pdets_fhr=Section1.objects.values_list('fhr') 
    pdets_hrs=Section1.objects.values_list('hrs') 
    for i in pdets_fhr:
        for j in i:
            #print(j)
            fhrl.append(j)
            print("fhrl",fhrl)

    for i in pdets_hrs:
        for j in i:
            #print(j)
            hrsl.append(j)
            print("hrsll",hrsl)        

    

        
    x1=[1,1.5,2]
    y1=[20,40,60]
    
    template = loader.get_template('Section1/sec1.html')
    chart=get_plot1(hrsl,fhrl)
    context={'chart':chart}
    return HttpResponse(template.render(context, request)) 


def Section2_view(request):
    if request.method=="POST":
        af=request.POST.get("amnio")
        moulding=request.POST.get("moulding")
        protein=request.POST.get("protein")
        acetone=request.POST.get("acetone")
        volume=request.POST.get("volume")
        obj3=Section2()
        obj3.amnioticfluid=af
        obj3.moulding=moulding
        obj3.protein=protein
        obj3.acetone=acetone
        obj3.volume=volume
        obj3.save()

        contractionsno=request.POST.get("cno")
        contractionsdu=request.POST.get("cduration")
        hour3=request.POST.get("hr3")
        oxytocin=request.POST.get("oxy")
        obj4=Section3()
        obj4.contractionsno=contractionsno
        #obj4.contractionsdur=contractionsdu
        obj4.chours=hour3
        obj4.oxytocin=oxytocin
        obj4.save()

    

    return render(request, "Section2\Section2.html")
from django.shortcuts import render , redirect
from.models import Member
from cat.models import Cat
from sitesetting.models import Sitesetting
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from ipware import get_client_ip

# Create your views here.

def fregister(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        ip , is_routable = get_client_ip(request)

        if ip is None:
            ip = "0,0,0,0"
       
        if password1 != password2:
            mgs = " پسورد ها مشابه نیست   "
            return render(request,'front/mgs.html' , {'mgs':mgs})
        
        if len(password1) < 8 :
            mgs = " طول پسورد مناسب نیست   "
            return render(request,'front/mgs.html' , {'mgs':mgs})

        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0

        for i in password1:
            if i > "0" and i <"9":
                count1 = 1
           
            if i > "a" and i <"z":
                count3 = 1
        
        if count1 == 1  and count3 == 1 :
            uname = email
            user =  User.objects.create_user(username=uname , password=password1)
            b=Member(username = uname , upass = password1 ,email=email , phone=phone , address=address , pip=ip , name=name )
            b.save()  
            if ip == Wish.ip :
                basketview = Wish.objects.all()
            return redirect('upanel')
        else:
            mgs = " پسورد قوی نیست   "
            return render(request,'front/mgs.html' , {'mgs':mgs})
    

    basketview = Wish.objects.all()
    cat=Cat.objects.all()
    mysetting = Mysetting.objects.get(pk=1)
    return render(request , 'front/register.html' , { 'basketview':basketview , 'mysetting':mysetting  , 'cat':cat})


def memberlist(request):

    member = Member.objects.all()
    mysetting = Mysetting.objects.get(pk=1)
    return render(request , 'back/memberlist.html' , {'member':member  , 'mysetting':mysetting})


def upanel(request ):

    member = Member.objects.all()
    mysetting = Mysetting.objects.get(pk=1)
    cat=Cat.objects.all()
    basketview= Wish.objects.all()
    return render(request , 'front/userpanel.html' , {'basketview':basketview , 'member':member , 'mysetting':mysetting , 'cat':cat})


def delmember(request,pk ):

    member = Member.objects.all()
    b=Member.objects.get(pk=pk)
    b.delete()
   
    return redirect('memberlist')


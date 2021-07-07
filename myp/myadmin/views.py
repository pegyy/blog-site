from django.shortcuts import render ,redirect
from.models import Myadmin
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

from cat.models import Cat
# Create your views here.


def newadmin(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            mgs = " پسورد ها مشابه نیست   "
            return render(request,'front/mgs.html' , {'mgs':mgs})
        
        if len(password1) < 8 :
            mgs = " طول پسورد مناسب نیست   "
            return render(request,'front/error.html' , {'mgs':mgs})

        count1 = 0
        count3 = 0

        for i in password1:
            if i > "0" and i <"9":
                count1 = 1
           
            if i > "a" and i <"z":
                count3 = 1
        
        if count1 == 1  and count3 == 1 :
            uname = email
            user =  User.objects.create_user(username=uname , password=password1)
            b=Myadmin(username = uname , upass = password1 ,email=email , name=name )
            b.save()  
            return redirect('admins')

        else:
            mgs = " پسورد قوی نیست"
            return render(request,'front/error.html' , {'mgs':mgs})

    admin=Myadmin.objects.all()
    return render(request , 'back/newadmin.html' , {'admin':admin})


def admins(request):
    admin=Myadmin.objects.all()

    return render(request , 'back/admins.html' , {'admin':admin})

def adlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        ptxt = request.POST.get('password')

        if username != "" or ptxt != "" :
            user = authenticate(username =username , password = ptxt)
            if user != None:
                login(request,user)
                return redirect( 'adpanel')
            else:
                mgs = "  این کاربر وجود ندارد "
                return render(request,'back/alogerror.html' , {'mgs':mgs})        
        else:
            mgs = "  همه ی موارد را وارد کنید "
            return render(request,'back/alogerror.html' , {'mgs':mgs})
                

    return render(request,'back/login.html')


def adpanel(request):

    cat = Cat.objects.all()

    return render(request , 'back/adpanel.html' , {'cat':cat})



def panel(request):



    cat = Cat.objects.all()
    pk=Cat.pk
    return render(request , 'back/panel.html' , {'cat':cat , 'pk':pk})
from django.shortcuts import render, redirect
import datetime
from main.dateconverter import shamsiDate
from.models import Cat
# Create your views here

def addcat(request):

    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
  
    today = shamsiDate(int(year),int(month),int(day))
    time = str(now.hour)+":"+str(now.minute)
    
    if request.method == 'POST':
        name=request.POST.get('name')
        if name =="":
            error=" نام دسته بندی را وارد کنید "
            return render(request,'back/error.html' , {'error':error})

        b=Cat(name=name , time_cat=time , date_cat=today)
        b.save()
        return redirect('catlist')
        
    return render(request, 'back/addcat.html')
    

def catlist(request):
    cat=Cat.objects.all().order_by('-pk')
    print("------------------------------------------------")
    pk=Cat.pk
    return render(request, 'back/catlist.html' , {'cat':cat , 'pk':pk})


def editcat(request , pk ):

    cat = Cat.objects.get(pk=pk)

    if request.method == 'POST':

        name=request.POST.get('name')
        if name =="":
            error=" نام دسته بندی را وارد کنید "
            return render(request,'back/error.html' , {'error':error})

        b = Cat.objects.get(pk=pk)

        b.name= name
        b.save()
        return redirect('catlist')


    cat = Cat.objects.get(pk=pk)
    return render(request , 'back/editcat.html' , {'cat':cat})





def deletecat(request,pk ):

    cat = Cat.objects.all()
    b = Cat.objects.get(pk=pk)
 
    b.delete()
   
    return redirect('catlist')
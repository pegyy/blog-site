from django.shortcuts import render , redirect
import datetime
from main.dateconverter import shamsiDate
from.models import Contact
from news.models import News
from cat.models import Cat
from main.models import Main
from django.core.mail import send_mail
from django.conf import settings
import smtplib
from sitesetting.models import Sitesetting

# Create your views here.

def contact(request):

    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
  
    today = shamsiDate(int(year),int(month),int(day))
    time = str(now.hour)+":"+str(now.minute)

    if request.method =='POST':
        name=request.POST.get('namecu')
        emailcu=request.POST.get('emailcu')
        mtext=request.POST.get('textcu')
        if name =="" or emailcu=="" or  mtext=="" :
            error="همه ی موارد را وارد کنید  "
            return render(request,'back/error.html' , {'error':error})
        b=Contact( namecu = name , emailcu=emailcu , textcu=mtext  , time_cu = time , date_cu=today)
        b.save()

        mgs = "ارسال شد! "
        mgs2 = "تشکر "
        setting = Sitesetting.objects.get(pk=1)
        cat=Cat.objects.all()
        return render(request , 'front/mgs.html' , {'mgs':mgs, 'mgs2':mgs2 ,'setting':setting , 'cat':cat})


    news=News.objects.all().order_by('-pk')
    cat=Cat.objects.all()
    setting = Sitesetting.objects.get(pk=1)
    contact=Contact.objects.all()

    return render(request , 'front/contact.html' ,{'news':news, 'cat':cat ,  'setting':setting  , 'contact':contact} )

def mgslist(request):
    pk=Contact.pk
    contact=Contact.objects.all().order_by('-pk')
    setting = Sitesetting.objects.get(pk=1)

    return render(request , 'back/mgslist.html' , { 'setting':setting , 'contact':contact , 'pk':pk})

def answer(request , pk ):

    contact = Contact.objects.get(pk=pk)
    if request.method =='POST':

        texta=request.POST.get('texta')
        if texta =="":
            error="متن پیام را وارد کنید  "
            return render(request,'back/error.html' , {'error':error})

        b= Contact.objects.get(pk=pk)

        b.texta= texta
        b.save()

        to_email = Contact.objects.get(pk=pk).emailcu

        SUBJECT = 'TEST MAIL'
        TEXT =  texta

        # Gmail Sign In
        gmail_sender = 'pegyy.me@gmail.com'
        gmail_passwd = 'dkwuzddrdzbgqlsu'

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_sender, gmail_passwd)

        BODY = '\r\n'.join(['To: %s' % to_email,
                    'From: %s' % gmail_sender,
                    'Subject: %s' % SUBJECT,
                    '', TEXT])

        try:
            server.sendmail(gmail_sender, [to_email], BODY)
            print ('email sent')
        except:
            print ('error sending mail')

        server.quit()
        mgs = " با موفقیت ارسال شد "
        return render(request , 'back/mgs.html' , {'mgs':mgs})

    setting = Sitesetting.objects.get(pk=1)
    contact = Contact.objects.get(pk=pk)

    return render(request , 'back/answer.html' , {'setting':setting,'pk':pk , 'contact':contact})

def deletemgs(request,pk ):

    contact=Contact.objects.all()
    b=Contact.objects.get(pk=pk)
    b.delete()
   
    return redirect('mgslist')


def getemail(request):

    if request.method=='POST':
        newsletters = request.POST.get('newsletters')

        b= Contact(newsletters=newsletters)
        b.save()

        return redirect('home')
    return render (request,'back/getemail.html')


def showmail(request):
    contact=Contact.objects.all().order_by('-pk')
    setting = Sitesetting.objects.get(pk=1)

    return render(request , 'back/emails.html' , { 'setting':setting , 'contact':contact })

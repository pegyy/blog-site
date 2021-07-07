from django.shortcuts import render , redirect
from.models import News
import datetime
from main.dateconverter import shamsiDate
import random
from cat.models import Cat
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.core.files.storage import FileSystemStorage
from django.utils.http import urlunquote
from sitesetting.models import Sitesetting
from comment.models import Comment
from itertools import chain
mysearch = ""
# Create your views here.

def addpost(request , pk ):

    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
  
    today = shamsiDate(int(year),int(month),int(day))

    time = str(now.hour)+":"+str(now.minute)

    date = str(year) + str(month) + str(day)
    randint=str(random.randint(1000,9999))
    rand = date + randint
    rand = int(rand)

    while len(News.objects.filter(rand=rand)) != 0 :
        
        randint=str(random.randint(1000,9999))
        rand = date + randint
        rand = int(rand)

    if request.method  == 'POST':
        title = request.POST.get('title')
        short_txt=request.POST.get('short_txt')
        text=request.POST.get('text')


        if title=="" or short_txt=="" or text=="" :
            error = "همه ی موارد خواسته شده را وارد کنید "
            return render(request,'back/error.html' , {'error':error})

        try:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url=fs.url(filename) 

            
        except:
            error = "عکس مدنظر را وارد کنید  "
            return render(request,'back/error.html' , {'error':error})

        catname = Cat.objects.get(pk=pk).name
        
        b=News(title=title , short_txt=short_txt, text = text ,date=today , time= time , pic= filename ,picurl=url ,catname=catname ,rand=rand)
        b.catid=pk
        b.save()
        mgs = " با موفقیت ثبت شد "
        return render(request , 'back/mgs.html' , {'mgs':mgs})

    doc1 = News.objects.all()
    cats = Cat.objects.get(pk=pk)
    cat=Cat.objects.all()
    return render(request , 'back/addpost.html'  , {'cat':cat,'cats':cats ,'doc1':doc1 ,'pk':pk })

def postlist(request , pk ):

    doc1s=News.objects.all().order_by('-pk')

    paginator = Paginator(doc1s , 6)
    page = request.GET.get('page')

    try:
        doc1 = paginator.page(page)

    except EmptyPage :

        doc1 = paginator.page(paginator.num_pages)

    except PageNotAnInteger :
        doc1 = paginator.page(1)

    cats = Cat.objects.get(pk=pk)
    cat=Cat.objects.all()
    return render(request, 'back/postlist.html' , {'doc1':doc1 , 'cat':cat , 'cats':cats})

def editnews(request,pk):
    news = News.objects.get(pk=pk)
    if request.method =='POST':
        title=request.POST.get('title')
        short_txt=request.POST.get('short_txt')
        text=request.POST.get('text')
        text2=request.POST.get('text2')
        text3=request.POST.get('text3')
        try:
            
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename= fs.save(myfile.name, myfile)
            url=fs.url(filename)
            b=News.objects.get(pk=pk)

            fss = FileSystemStorage()
            fss.delete(b.pic)

            b.pic= filename
            b.picurl = url
            b.short_txt = short_txt
            b.title = title
            b.text=text
            b.text2 = text2
            b.text3 = text3
            b.save()
            mgs = "    ویرایش انجام شد  "
            return render(request , 'back/mgs.html' , {'mgs':mgs})
        except: 
            b=News.objects.get(pk=pk)
            b=News.objects.get(pk=pk)
            b.short_txt = short_txt
            b.title = title
            b.text=text
            b.text2 = text2
            b.text3 = text3
            b.save()
            mgs = "    ویرایش انجام شد  "
            return render(request , 'back/mgs.html' , {'mgs':mgs})
        try:
            myfile2 = request.FILES['myfile2']
            fs2 = FileSystemStorage()
            filename2 = fs2.save(myfile2.name , myfile2)
            url2=fs2.url(filename) 
            b=News.objects.get(pk=pk)
            fss = FileSystemStorage()
            fss.delete(b.pic)
            b.pic2= filename2
            b.picurl2 = url2
            b=News.objects.get(pk=pk)
            b.short_txt = short_txt
            b.title = title
            b.text=text
            b.text2 = text2
            b.text3 = text3
            b.save()
            mgs = "    ویرایش انجام شد  "
            return render(request , 'back/mgs.html' , {'mgs':mgs})
        except:
            b=News.objects.get(pk=pk)
            b=News.objects.get(pk=pk)
            b.short_txt = short_txt
            b.text=text
            b.title = title
            b.text2 = text2
            b.text3 = text3
            b.save()
            mgs = "    ویرایش انجام شد  "
            return render(request , 'back/mgs.html' , {'mgs':mgs})

    return render(request,'back/editpost.html',{'news':news ,'pk':pk  })

def deletenews(request,pk ):

    news=News.objects.all()
    b=News.objects.get(pk=pk)
    fs=FileSystemStorage()
    fs.delete(b.pic)
    b.delete()
    mgs = "پست مورد نظر حذف شد"
    return render(request , 'back/mgs.html' , {'mgs':mgs})

def post(request , word):
    try:
        word=urlunquote(word)
        snews = News.objects.get(title=word)
        snews.show = snews.show + 1
        snews.save()


    except:
        print(" except ")
    news = News.objects.get(title=word)
    pk= News.pk
    cat = Cat.objects.all()
    lastnews = News.objects.all().order_by('-pk')
    like =News.objects.all().order_by('-show')
    similar = News.objects.all()[:3]
    other = News.objects.all()[:6]
    setting = Sitesetting.objects.get(pk=1)
    comment = Comment.objects.all()

    return render(request , 'front/post.html' , { 'comment':comment ,'setting':setting, 'other':other , 'like':like , 'pk':pk ,'cat':cat ,'news':news ,'similar':similar, 'lastnews':lastnews })

def film(request):
    other = News.objects.all()[:7]
    cat = Cat.objects.all()
    news=News.objects.all()
    last = News.objects.all().order_by('-pk')[:2]
    view = News.objects.all().order_by('-show')[:2]
    setting = Sitesetting.objects.get(pk=1)
    sililar = News.objects.all()[:3]


    doos=News.objects.all().order_by('-pk')

    paginator = Paginator(doos , 1)
    page = request.GET.get('page')

    try:
        doo = paginator.page(page)

    except EmptyPage :

        doo = paginator.page(paginator.num_pages)

    except PageNotAnInteger :
        doo = paginator.page(1)

    cat=Cat.objects.all()

    return render(request , 'front/film.html', { 'doo':doo ,'sililar':sililar ,'setting':setting,'other':other,'news':news , 'last':last ,'view':view , 'cat':cat})

def interview(request):
    other = News.objects.all()[:6]
    last = News.objects.all().order_by('-pk')[:2]
    cat = Cat.objects.all()
    news=News.objects.all()
    view = News.objects.all().order_by('-show')[:2]
    setting = Sitesetting.objects.get(pk=1)
    sililar = News.objects.all()[:3]

    return render(request , 'front/interview.html' ,{'sililar':sililar ,'setting':setting,'other':other,'news':news , 'view':view , 'cat':cat , 'last':last })


def music(request):
    last = News.objects.all().order_by('-pk')[:2]
    cat = Cat.objects.all()
    news=News.objects.all()
    view = News.objects.all().order_by('-show')[:2]
    other = News.objects.all()[:6]
    setting = Sitesetting.objects.get(pk=1)
    sililar = News.objects.all()[:3]
    return render(request , 'front/music.html' , { 'sililar':sililar , 'setting':setting, 'other':other,'news':news ,'cat':cat ,'last':last , 'view':view})

def news(request):
    other = News.objects.all()[:6]
    setting = Sitesetting.objects.get(pk=1)
    news=News.objects.all()
    cat = Cat.objects.all()
    sililar = News.objects.all()[:3]

    return render(request , 'front/news.html' , {'sililar':sililar ,'setting':setting,'other':other,'news':news , 'cat':cat})



def alls(request):
    cat=Cat.objects.all()
    news=News.objects.all().order_by('-pk')
    setting = Sitesetting.objects.get(pk=1)
    other = News.objects.all()[:6]

    return render(request, 'front/all.html' ,{'other':other ,'setting':setting, 'news':news , 'cat':cat })

def nsearch(request):
    if request.method == 'POST':
        
        txt = request.POST.get('txt')
        mysearch=txt

        a = News.objects.filter(title__contains=txt)
        b = News.objects.filter(short_txt__contains=txt)
        c = News.objects.filter(text__contains=txt)
        d = News.objects.filter(text2__contains=txt)
        e = News.objects.filter(text3__contains=txt)


        alls = list(chain(a,b,c,d,e))
        alls = list(dict.fromkeys(alls))
        

    cat=Cat.objects.all()
    news=News.objects.all().order_by('-pk')
    setting = Sitesetting.objects.get(pk=1)
    other = News.objects.all()[:6]
    return render(request , 'front/all.html' ,{ 'other':other , 'setting':setting,'news':news,'cat':cat,'alls':alls})



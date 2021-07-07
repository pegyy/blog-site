from django.shortcuts import render
from.models import Sitesetting
from cat.models import Cat
from django.core.files.storage import FileSystemStorage
# Create your views here.

def mysetting(request):
    if request.method == 'POST':
        name=request.POST.get('sitename')
        tlg=request.POST.get('tlg')
        email=request.POST.get('email')
        Insta=request.POST.get('insta')
        address=request.POST.get('address')
        contact_txt = request.POST.get('contact_txt')
 
        b = Sitesetting.objects.get(pk=1)
        b.sitename=name
        b.tlg = tlg
        b.insta = Insta
        b.email = email
        b.address=address

        b.contact_txt = contact_txt
        b.save()
        mgs = " با موفقیت ثبت شد "
        return render(request , 'back/mgs.html' , {'mgs':mgs})
    cat=Cat.objects.all()
    setting=Sitesetting.objects.get(pk=1)
    return render(request , 'back/setting.html' , {'cat':cat ,'setting':setting})


def logoset(request):
    if request.method == 'POST':
        try:
            myfile=request.FILES['myfile']
            fs=FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url=fs.url(filename)
            b = Sitesetting.objects.get(pk=1)
        except:
            logo="-"
            logourl = "-"  

        b.logo = filename
        b.logourl = url
        b.save()
        
    setting=Sitesetting.objects.get(pk=1)
    return render(request , 'back/logoset.html',{'setting':setting})

def foot(request):

    if request.method == 'POST':

        bio =request.POST.get('biotext')
        tag = request.POST.get('tag')

        b = Sitesetting.objects.get(pk=1)

        b.biotext = bio
        b.tag = tag
        b.save()
        mgs = " با موفقیت ثبت شد "
        return render(request , 'back/mgs.html' , {'mgs':mgs})

    setting=Sitesetting.objects.get(pk=1)

    return render(request  , 'back/footsetting.html' , {'setting':setting})



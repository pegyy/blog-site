from django.shortcuts import render
from.models import Main
from cat.models import Cat
from news.models import News
from sitesetting.models import Sitesetting
# Create your views here.




def home(request):
    news = News.objects.all()[:4]
    setting = Sitesetting.objects.get(pk=1)
    last = News.objects.all().order_by('-pk')
    last2 = News.objects.all().order_by('-pk')[:2]
    cat = Cat.objects.all()
    other = News.objects.all()[:3]
    pk = Cat.pk
    return render( request ,'front/home.html' , {'other':other , 'cat':cat , 'last':last ,'pk':pk , 'setting':setting , 'news':news , 'last2':last2})





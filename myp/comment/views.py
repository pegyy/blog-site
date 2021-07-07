from django.shortcuts import render
import datetime
from main.dateconverter import shamsiDate
from.models import Comment
from sitesetting.models import Sitesetting



def addcomment(request , pk):

    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    today = shamsiDate(int(year),int(month),int(day))
    time = str(now.hour)+":"+str(now.minute)
    if request.method == 'POST':
        pname=request.POST.get('pname')
        pemail=request.POST.get('pemail')
        comment_txt=request.POST.get('comment_txt')

        b = Comment( pname=pname , pemail=pemail ,comment_txt=comment_txt , date=today , time=time  , postid=pk)
        b.save()
        mgs = "نظر شما ثبت شد "
        return render(request , 'front/mgs.html' , {'mgs':mgs})
    comment = Comment.objects.all()
    setting = Sitesetting.objects.get(pk=1)

    return render(request , 'front/posts.html' ,{'setting':setting , 'comment':comment})
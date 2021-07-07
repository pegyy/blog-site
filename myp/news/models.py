from __future__ import unicode_literals
from django.db import models

from django.shortcuts import reverse

# Create your models here.

class News(models.Model):

    
    title = models.CharField(max_length=200 , default="-")
    
    time = models.CharField(max_length=100 , default="-")
    date = models.CharField(max_length=100 , default="-")

    short_txt = models.TextField(max_length=300, default="-")
    
    text = models.TextField(max_length=3000, default="-") 
    text2 = models.TextField(max_length=3000, default="-") 
    text3 = models.TextField(max_length=3000, default="-") 

    pic = models.TextField(max_length=100 , default="-")
    picurl = models.TextField(max_length=100, default="-")

    pic2 = models.TextField(max_length=100 , default="-")
    picurl2 = models.TextField(max_length=100, default="-")

    pic3 = models.TextField(max_length=100 , default="-")
    picurl3 = models.TextField(max_length=100, default="-")

    pic4 = models.TextField(max_length=100 , default="-")
    picurl4 = models.TextField(max_length=100, default="-")

    pic5 = models.TextField(max_length=100 , default="-")
    picurl5 = models.TextField(max_length=100, default="-")

    pic6 = models.TextField(max_length=100 , default="-")
    picurl6 = models.TextField(max_length=100, default="-")

    pic7 = models.TextField(max_length=100 , default="-")
    picurl7 = models.TextField(max_length=100, default="-")

    pic8 = models.TextField(max_length=100 , default="-")
    picurl8 = models.TextField(max_length=100, default="-")

    pic9 = models.TextField(max_length=100 , default="-")
    picurl9 = models.TextField(max_length=100, default="-")

    pic10 = models.TextField(max_length=100 , default="-")
    picurl10 = models.TextField(max_length=100, default="-")

    writer = models.TextField(max_length=100,default="-")
    show= models.IntegerField(default=0)

    catid= models.IntegerField(default=0)
    catname=models.CharField(max_length=40 , default="-")

    rand=models.IntegerField(default=0)



    def __str(self):
        return self.title + "|" + str(self.pk)
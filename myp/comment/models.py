from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Comment(models.Model):

    postid = models.TextField(default=0)

    comment_txt = models.TextField(max_length=100,default="-")

    pname = models.TextField(max_length=100,default="-")

    pemail = models.TextField(max_length=300 , default="-")

    ctype = models.IntegerField(default=0)

    date = models.TextField(max_length=100,default="-")

    time = models.TextField(max_length=100 ,default="-")

    comment_title = models.TextField(max_length=200 , default="-")
 

    def __str(self):
        return self.pname + "|" + str(self.pk)






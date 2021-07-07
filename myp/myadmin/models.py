from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Myadmin(models.Model):

    name = models.TextField(max_length=100 , default="-")
    upass = models.TextField(max_length=100 , default="-")
    username = models.TextField(max_length=100 , default="-")
    email = models.TextField(max_length=100, default="-")
    phone = models.TextField(max_length=100, default="-")
    address = models.TextField(max_length=100, default="-")
    pic = models.TextField(max_length=100 , default="-")
    picurl = models.TextField(max_length=100, default="-")

    aip=models.TextField(max_length=100,default="-")

    bio=models.TextField(max_length=100,default="-")

    # number

    number = models.TextField(max_length=100 , default=0 )

    def __str(self):
        return self.name + "|" + str(self.pk)

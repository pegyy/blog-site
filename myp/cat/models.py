from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Cat(models.Model):

    name = models.TextField(max_length=100 , default="-")

    count = models.IntegerField(default=0)

    time_cat = models.CharField(max_length=100 ,default="-" )
    date_cat =models.CharField(max_length=100 , default="-")


    def __str(self):
        return self.name + "|" + str(self.pk)
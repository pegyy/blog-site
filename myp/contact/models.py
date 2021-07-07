from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Contact(models.Model):

    namecu = models.TextField(max_length=100 )
    emailcu = models.TextField(max_length=100 )
    textcu = models.TextField(max_length=100)

    time_cu = models.CharField(max_length=100)
    date_cu =models.CharField(max_length=100)

    #answer 

    texta = models.TextField(max_length=200 , default="-")


    newsletters = models.TextField(max_length=300 , default="-")


    def __str(self):
        return self.namecu + "|" + str(self.pk)
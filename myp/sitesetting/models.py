from django.db import models

# Create your models here.



class Sitesetting(models.Model):

    sitename=models.CharField(max_length=100 )
    email=models.CharField(max_length=100)
    insta=models.CharField(max_length=100)
    tlg = models.CharField(max_length=100)
    address=models.CharField(max_length=100)


    # admin info 
    name = models.TextField(max_length=100 , default="-")
    email = models.TextField(max_length=100 , default="-")
    bio = models.TextField(max_length=100 , default="-")

    contact_txt = models.TextField(max_length=500 , default="-")
    



    logo = models.TextField(max_length=100)
    logourl = models.TextField(max_length=100)

    banner1 = models.TextField(max_length=100)
    banner1url = models.TextField(max_length=100 )

    banner2 = models.TextField(max_length=100, default="-")
    banner2url = models.TextField(max_length=100 , default="-")

    banner3 = models.TextField(max_length=100, default="-")
    banner3url = models.TextField(max_length=100 , default="-")

    tag = models.TextField(max_length=500 , default="-")

    biotext= models.TextField(max_length=300 )


    def __str(self):
        return self.sitename + "|" + str(self.pk)
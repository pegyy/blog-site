from django.urls import path,include
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns=[
   path('panel/setting/', views.mysetting,name='mysetting'),
   path('panel/footsetting/' , views.foot , name='foot'),
   path('panel/logoset/' , views.logoset , name='logoset'),


]
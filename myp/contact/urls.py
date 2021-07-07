from django.urls import path,include
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns=[
    path('contact/',views.contact,name='contact'),
    path('panel/answer/<pk>/' , views.answer , name='answer'),
    path('panel/mgslist/' , views.mgslist , name='mgslist'),
    path('panel/mgs/del/<pk>/',views.deletemgs,name='deletemgs'), 
    path('panel/getemail/' , views.getemail , name='getemail'),
    path('panel/showmail/',views.showmail , name = 'showmail'),

]
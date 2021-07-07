from django.urls import path,include
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns=[
   path('panel/memberlist/' , views.memberlist , name='memberlist'),

   path('register/',views.fregister,name='fregister'),

   path('userpanel/' , views.upanel , name='upanel'),

   path('delmember/<pk>/' , views.delmember , name='delmember'),

]
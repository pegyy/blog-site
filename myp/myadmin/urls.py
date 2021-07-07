from django.urls import path,include
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns=[

   path('panel/newadmin/' , views.newadmin , name ='newadmin'),
   path('panel/admins/',views.admins , name='admins'),
   path('login/' , views.adlogin , name = 'adlogin'),
   path('adpanel/',views.adpanel , name='adpanel'),
   path('panel/',views.panel,name='panel'),

]
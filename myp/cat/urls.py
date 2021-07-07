from django.urls import path,include
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns=[
    
    path('panel/addcat/',views.addcat,name='addcat'),
    path('panel/catlist/',views.catlist,name='catlist'),
    
    path('panel/editcat/<pk>',views.editcat , name = 'editcat'),
    path('panel/deletecat/<pk>',views.deletecat , name = 'deletecat'),
]
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static 
from . import views

urlpatterns = [
    path('addpost/<pk>', views.addpost,name='addpost'),
    path('panel/postlist/<pk>/' , views.postlist , name='postlist'),
    path('panel/news/edit/<pk>/',views.editnews,name='editnews'),  
    path('post/<word>/' , views.post , name ='post'),
    path('panel/news/del/<pk>/',views.deletenews,name='deletenews'),  
    path('nsearch/' , views.nsearch , name = 'nsearch'),
    path('film/',views.film , name='film'),
    path('interview/',views.interview , name='interview'),
    path('music/',views.music , name='music'),
    path('news/',views.news , name='news'),
    path('all/' , views.alls , name = 'alls'),
    path('nsearch/' , views.nsearch , name = 'nsearch'),
]
from django.urls import path
from .views import *

urlpatterns=[
    path('',index, name='index'),
    path('article/<int:id>', article_detail, name='article'),
    path('sport/',sport_news,name='sport'),
    path('local/',local_news,name='local'),
    path('world/',world_news,name='world')
]

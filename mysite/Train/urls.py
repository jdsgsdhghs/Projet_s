
from . import  views
from django.urls import path
urlpatterns = [
    path('index', views.index, name="index"),
    path('show/<train_id>', views.show, name='show'),
    path('random', views.random, name='random'),
    
    
]
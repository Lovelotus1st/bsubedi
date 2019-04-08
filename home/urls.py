from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home1', views.index1, name='index'),
    path('home2', views.index2, name='index'),
    path('home3', views.index3, name='index'),
]
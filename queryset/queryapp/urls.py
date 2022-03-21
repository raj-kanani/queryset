
from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path('home/', views.home),
    path('index/', views.index),
    path('base/', views.base),
    path('base2/', views.base2),

]
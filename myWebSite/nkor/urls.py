from django.urls import path
from django.shortcuts import render

from . import views

urlpatterns = [
    path('', views.nkor_view, name='nkor_view'),
    path('mirror', views.mirror_view, name='mirror_view'),
]
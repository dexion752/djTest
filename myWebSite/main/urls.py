from django.urls import path
from django.shortcuts import render

from . import views

urlpatterns = [
    #  path('', views.index, name=''),
    path('', views.main_view, name='main_view'),
    path('mirror', views.mirror_view, name='mirror_view'),
    # path('nkorea', views.testdata_view, name='testdata_view'),
]

from django.contrib import admin
from django.urls import path, re_path
from . import views

from django.conf.urls import url, include


urlpatterns = [
    path('add/', views.AddView.as_view(), name='addView'),
    path('compare/', views.CompareView.as_view(), name='compareView'),
]

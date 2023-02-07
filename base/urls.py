from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path('student/', views.StudentView.as_view()),
    path('', views.index),
]

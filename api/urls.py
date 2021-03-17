"""
API URL Configuration
"""
from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('todos/completed', views.TodoCompletedList.as_view()),
]

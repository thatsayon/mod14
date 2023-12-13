from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name="Form"),
    path('model/', views.model, name="Model"),
]
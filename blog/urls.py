from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='blog-home'),
    path('problems/', views.problems,name='blog-problems'),
    path('about/', views.about,name='blog-about'),
]
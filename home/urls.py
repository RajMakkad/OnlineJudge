from django.urls import path
from . import views

urlpatterns = [
    path('', views.problems, name='home'),
    path('problems/', views.problems, name='problems'),
    path('about/', views.about, name='about'),
]

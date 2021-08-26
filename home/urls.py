from django.urls import path
from . import views

urlpatterns = [
    path('', views.problems, name='home'),
    path('problems/', views.problems, name='problems'),
    path('problem_page/<int:prob_id>', views.problem_page, name='problem_page'),
    path('submit/<int:prob_id>',views.submit,name='submit_n'),
    path('about/', views.about, name='about'),
]

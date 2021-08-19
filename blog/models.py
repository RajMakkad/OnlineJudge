from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User


class Problem(models.Model) :
    Statement = models.TextField()
    Name = models.CharField(max_length=200)
    Code = models.TextField()
    Difficulty = models.CharField(max_length=200)

class Solution(models.Model) :
    Problem = models.ForeignKey(User, on_delete=models.CASCADE)
    Verdict = models.CharField(max_length=200)
    Time_Submitted = models.DateTimeField(auto_now=timezone.now())

class Test_Case(models.Model) :
    Input = models.CharField(max_length=200)
    Output = models.CharField(max_length=200)
    Problem = models.ForeignKey(User, on_delete=models.CASCADE)

# class Post(models.Model) :
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     date_posted = models.DateTimeField(default=timezone.now)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) :
         return self.title



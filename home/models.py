from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Problem(models.Model):
    Statement = models.TextField()
    Name = models.CharField(max_length=200)
    Code = models.TextField()
    Difficulty = models.CharField(max_length=200)


class Solution(models.Model):
    Problem = models.ForeignKey(User, on_delete=models.CASCADE)
    Verdict = models.CharField(max_length=200)
    Time_Submitted = models.DateTimeField(auto_now=timezone.now())


class TestCase(models.Model):
    Input = models.CharField(max_length=200)
    Output = models.CharField(max_length=200)
    Problem = models.ForeignKey(User, on_delete=models.CASCADE)

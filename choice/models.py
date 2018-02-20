from django.contrib.auth.models import User
from django.db import models


class Exam(models.Model):
    name = models.CharField(max_length=100, default="")
    guru = models.CharField(max_length=50)
    kkm = models.IntegerField()
    tanggal = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.name


class Question(models.Model):
    question = models.TextField(max_length=200, default="")
    option1 = models.CharField(max_length=50, default="")
    option2 = models.CharField(max_length=50, default="")
    option3 = models.CharField(max_length=50, default="")
    option4 = models.CharField(max_length=50, default="")
    answer = models.CharField(max_length=50, default="")
    exam = models.ForeignKey(Exam)

    def __str__(self):
        return self.question


class Score(models.Model):
    user = models.ForeignKey(User)
    mata_pelajaran = models.ForeignKey(Exam)
    score = models.IntegerField()
    tanggal = models.DateTimeField(auto_now_add=True, auto_now=False)
    lulus = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

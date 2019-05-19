from django.db import models


class User(models.Model):
    id = models.CharField(max_length=128, primary_key=True)
    name = models.CharField(max_length=128)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    time = models.DateTimeField(auto_now_add=True)
    picture = models.CharField(max_length=256)

class Deskstate(models.Model):
    num = models.CharField(max_length=128, primary_key=True)
    state = models.CharField(max_length=128)
    time = models.DateTimeField(auto_now_add=True)
    it = models.CharField(max_length=128)


class Er(models.Model):
    num = models.CharField(max_length=128, primary_key=True)
    time = models.DateTimeField(auto_now_add=True)

class Id(models.Model):
    num = models.CharField(max_length=128)
    id = models.CharField(max_length=128, primary_key=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self

    class Meta:
        ordering = ['time']
        verbose_name = '用户'
        verbose_name_plural = '用户'

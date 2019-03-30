from django.db import models


class User(models.Model):
    id = models.CharField(max_length=128, primary_key=True)
    name = models.CharField(max_length=128)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id

    class Meta:
        ordering = ['time']
        verbose_name = '用户'
        verbose_name_plural = '用户'

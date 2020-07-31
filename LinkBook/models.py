from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.utils import timezone
class Book(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} LinkBook'


class Link(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField()
    description = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.name} link'





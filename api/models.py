from django.db import models
from django.contrib.auth.models import AbstractUser

STATUS_CHOICES = {
    ('To_Read', 'To Read'),
    ('Reading', 'Reading'),
    ('Read', 'Read')
}

class User(AbstractUser):
    pass

class Book(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='books', null=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    author = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='')


class Note(models.Model):
    book = models.ForeignKey(to=Book, on_delete=models.CASCADE, related_name='notes')
    time_stamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    note = models.TextField(max_length=1000)
    page_number = models.CharField(max_length=5, null=True, blank=True)
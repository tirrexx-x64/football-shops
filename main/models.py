# models.py
from django.db import models
from django.contrib.auth.models import User
import uuid

class Product(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
  
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField(blank=True)
    thumbnail = models.URLField(blank=True)
    category = models.CharField(max_length=100, blank=True)
    is_featured = models.BooleanField(default=False)
    stock = models.IntegerField(default=0)
    brand = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable = False)
    title = models.CharField(max_length=255)


    def __str__(self):
        return self.title
    

class Author(models.Model):
    bio = models.TextField()
    books = models.ManyToManyField(Book, related_name='authors')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
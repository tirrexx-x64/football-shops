import uuid
from django.db import models

class Product(models.Model):
    id = models.UUIDField(
    primary_key=True,
    default=uuid.uuid4,
    editable=False
)

    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField(blank=True)
    thumbnail = models.URLField(blank=True)
    category = models.CharField(max_length=100, blank=True)
    is_featured = models.BooleanField(default=False)
    stock = models.IntegerField(default=0)
    brand = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

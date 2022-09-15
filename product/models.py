from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.CharField(max_length=100)
    price = models.IntegerField(null=False, blank=False)
    image = models.ImageField(default='default.jpg', upload_to='post_image/')
    quantity = models.IntegerField(null=False, blank=False)
    date_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


from django.contrib.auth.models import User
from rest_framework import serializers

from product.models import Product


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'author', 'name', 'price')
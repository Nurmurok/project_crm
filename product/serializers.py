from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product, Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'category', 'name','description', 'price', 'image', 'quantity', 'post_date']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class SaleSerializer(serializers.ModelSerializer):
    sum = serializers.IntegerField(required=False)
    class Meta:
        model = Product
        fields = ['price','quantity','sum']

from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render
from rest_framework import filters, permissions, response, generics
from rest_framework.generics import ListAPIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Count

from product.models import Product
from product.serializers import ProductSerializer
from user.serializers import UserSerializer
from .serializers import UserListSerializer, ProductListSerializer


class UserListApiView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


    filter_backends = [filters.SearchFilter]
    search_fields = ['username']
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['username', 'id']


class ProductListApiView(ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Product.objects.all()

    serializer_class = ProductListSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['price','date_time']
    filterset_fields = ['category']



class Count(ListAPIView):
    permission_classes = [permissions.AllowAny]
    parser_classes = [JSONParser]

    def get_object(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, id):
        user = self.get_object(id)

        posts = Product.objects.filter(user_id=id)
        serializer = UserSerializer(user)
        serializer2 = ProductSerializer(posts, many=True)
        data = serializer.data
        data['posts'] = serializer2.data
        data['quantity_of_posts'] = posts.count()

        return Response(data)




class Statistics(APIView):
    def get(self, request):
        users = User.objects.all()
        user_count = len(users)
        products = Product.objects.all()
        product_count = len(products)
        price_list = []
        revenue_list = []
        for product in products:
            price_list.append(product.price)
        revenue = product.price * product.quantity
        revenue_list.append(revenue)
        all_revenue = sum(revenue_list)
        avg_price = sum(price_list) / len(price_list)
        min_price = min(price_list)
        max_price =max((price_list))
        data = {
            "user_count": user_count,
            "product_count": product_count,
            "min_price": min_price,
            "max_price": max_price,
            "avg_price": avg_price,
            "all_sum": all_revenue,
        }
        return Response(data)


from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.parsers import JSONParser
from django.db.models import Q
from rest_framework.response import Response

from user.serializers import UserSerializer
from .models import Product, Category
from rest_framework.views import APIView
from .serializers import ProductSerializer, CategorySerializer, SaleSerializer
from rest_framework import permissions, status, pagination, viewsets, generics
from django.core.paginator import Paginator
from user.permissions import IsOwnerOrReadOnly, AnonPermissionOnly


class ProductListApiView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self,  request):
        products = Product.objects.all()
        paginator = Paginator(products, 5)
        page_num = self.request.query_params.get('page')
        print(page_num)
        serializers = ProductSerializer(paginator.page(page_num), many=True)
        return Response(serializers.data)


class ProductCreateApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializers = ProductSerializer(data=request.data)
        if serializers.is_valid():
           serializers.save()
           return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, id):
        try:
            return Product.objects.get(id=id)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, id):
        post = self.get_object(id)
        serializers = ProductSerializer(post)
        data = serializers.data
        return Response(data)


class ProductUpdateApiView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get_object(self, id):
        try:
            return Product.objects.get(id=id)
        except Product.DoesNotExist:
            raise Http404

    def put(self, requests,id):
        post = self.get_object(id)
        serializer = ProductSerializer(post, data=requests.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDestroyApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self, id):
        try:
            return Product.objects.get(id=id)
        except Product.DoesNotExist:
            raise Http404

    def delete(self, requests, id):
        post = self.get_object(id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class CategoryListApiView(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self,  request):
        category = Category.objects.all()
        paginator = Paginator(category, 1)
        page_num = self.request.query_params.get('page')
        print(page_num)
        serializers = CategorySerializer(paginator.page(page_num), many=True)
        return Response(serializers.data)


class CategoryCreateApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializers = CategorySerializer(data=request.data)
        if serializers.is_valid():
           serializers.save()
           return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDestroyApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, id):
        try:
            return Category.objects.get(id=id)
        except Category.DoesNotExist:
            raise Http404

    def delete(self, requests, id):
        category = self.get_object(id)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FilterByCategory(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [JSONParser]

    def get_object(self, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, name):
        category = self.get_object(name)
        product = Product.objects.filter(category__name=name)
        serializer = CategorySerializer(category)
        serializer2 = ProductSerializer(product, many=True)
        data = serializer.data
        data['products'] = serializer2.data

        return Response(data)

#не работает
class FilterByPrice(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        max_price = self.request.query_params.get('price')
        min_price = self.request.query_params.get('price')

        queryset = queryset.filter(price__range=(min_price,max_price))
        return queryset


# как вывести только продукты без данных юзера
class FilterByUserid(APIView):
    permission_classes = [permissions.AllowAny]
    parser_classes = [JSONParser]

    def get_object(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, id):
        user = self.get_object(id)
        posts = Product.objects.filter(author_id=id)
        serializer = UserSerializer(user)
        serializer2 = ProductSerializer(posts, many=True)
        data = serializer.data
        data['posts'] = serializer2.data
        data['quantity_of_posts'] = posts.count()
        return Response(data)

class UserSaleApiView(APIView):
    permission_classes = [permissions.AllowAny]
    parser_classes = [JSONParser]

    def get_object(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, id):
        user = self.get_object(id)
        posts = Product.objects.filter(author_id=id)
        serializer = UserSerializer(user)

        serializer2 = SaleSerializer(posts, many=True)
        data = serializer.data
        data['sale'] = serializer2.data
        # dict=data['sale']
        # sale = len(data['sale'])
        # i=0
        # while i in dict :
        #     price= data['sale'][:][1]['price']
        #     quantity= data['sale'][:][1]['quantity']
        #     sum = price*quantity
        #     print((sum))

        return Response(data)


from django.core.paginator import Paginator
from django.http import Http404
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from product.models import Product
from product.serializers import ProductSerializer
from .serializers import MyTokenObtainPairSerializer, AccountSerializer
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from .permissions import AnonPermissionOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics
from .serializers import UserSerializer
from rest_framework import permissions, status
from .models import Account
from rest_framework.generics import (
    CreateAPIView, ListAPIView,

)


class MyObtainPairView(TokenObtainPairView):
    permission_classes = (AnonPermissionOnly,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    parser_classes = [JSONParser]

    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        serializer2 = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create(
                username=request.data['username']
            )
            user.set_password(request.data['password'])
            user.save()
            account = Account.objects.create(
                user=user,
                phone_number=request.data['phone_number']
            )
            account.save()
            print(request.data['password'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#список с пагинацией, filter by username, em
class UserListView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'email']


class UserDetailApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
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
        data['products'] = serializer2.data
        data['quantity_of_posts'] = posts.count()
        return Response(data)


class UserDestroyApiView(APIView):
    permission_classes = [permissions.IsAdminUser]
    def get_object(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            raise Http404

    def delete(self, requests, id):
        user = self.get_object(id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




from django.core.paginator import Paginator
from django.http import Http404
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from product.models import Product
from product.serializers import ProductSerializer
from .serializers import MyTokenObtainPairSerializer
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from .permissions import AnonPermissionOnly
from .serializers import UserSerializer
from rest_framework import permissions, status
from rest_framework.generics import (
    CreateAPIView,

)


class MyObtainPairView(TokenObtainPairView):
    permission_classes = (AnonPermissionOnly,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AnonPermissionOnly,)
    serializer_class = RegisterSerializer


class UserListView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        users = User.objects.all()
        paginator = Paginator(users, 5)
        page_num = self.request.query_params.get('page')

        serializers = UserSerializer(paginator.page(page_num), many=True)
        return Response(serializers.data)


class UserDetailApiView(APIView):
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





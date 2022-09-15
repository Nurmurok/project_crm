from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView
)

from accounting.views import UserListApiView, ProductListApiView,Statistics

urlpatterns = [
    path('users/', UserListApiView.as_view(), name='users'),
    path('products/', ProductListApiView.as_view(), name='products'),

    path('statistics/', Statistics.as_view(), name='statistics')

]

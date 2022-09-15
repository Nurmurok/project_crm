from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView
)

from accounting.views import UserListApiView, ProductListApiView, AvgPriceListApiView, AllRrevenueListApiView,MaxPrice,MinPrice,PostCount

urlpatterns = [
    path('users/', UserListApiView.as_view(), name='users'),
    path('products/', ProductListApiView.as_view(), name='products'),
    path('avg_price/', AvgPriceListApiView.as_view(), name='avg_price'),
    path('all_revenue/', AllRrevenueListApiView.as_view(), name='all_revenue'),
    path('max_price/', MaxPrice.as_view(), name='max_price'),
    path('min_price/', MinPrice.as_view(), name='min_price'),
    path('post_count/', PostCount.as_view(), name='post_count'),
    path('user_count/', PostCount.as_view(), name='user_count'),

]

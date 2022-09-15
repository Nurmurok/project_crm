from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView
)
from user.views import (
    RegisterAPIView,
    MyObtainPairView,
    UserListView,
    UserDetailApiView,
    UserDestroyApiView


)


urlpatterns = [
    path('login/', MyObtainPairView.as_view(), name='token_obtain_pair'),
    path('list/', UserListView.as_view(), name='list'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('delete/<int:id>/', UserDestroyApiView.as_view(), name='user-list'),
    path('detail/<int:id>/', UserDetailApiView.as_view(), name='user-list')
]

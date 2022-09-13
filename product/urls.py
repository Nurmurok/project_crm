from django.urls import path
from .views import(
    ProductListApiView,
    ProductCreateApiView,
    ProductDetailApiView,
    ProductUpdateApiView,
    ProductDestroyApiView,
    CategoryListApiView,
    CategoryCreateApiView,
    FilterByCategory,
    CategoryDestroyApiView,
    FilterByPrice,
    FilterByUserid,
)

urlpatterns = [
    path('list/', ProductListApiView.as_view(), name='prod-list'),
    path('create/', ProductCreateApiView.as_view(), name='prod-create'),
    path('detail/<int:id>/', ProductDetailApiView.as_view(), name='detail'),
    path('update/<int:id>/', ProductUpdateApiView.as_view(), name='update'),
    path('delete/product/<int:id>/', ProductDestroyApiView.as_view(), name='delete'),
    path('category_list/', CategoryListApiView.as_view(), name='cat-list'),
    path('cat_create/', CategoryCreateApiView.as_view(), name='cat-create'),
    path('delete/category/<int:id>/', CategoryDestroyApiView.as_view(), name='cat-create'),
    path('filter_by_category/<slug:name>/', FilterByCategory.as_view(), name='filter-cat'),
    path('filter_by_price/', FilterByPrice.as_view(), name='filter-price'),
    path('filter_by_user_id/<int:id>/', FilterByUserid.as_view(), name='filter-username'),


]
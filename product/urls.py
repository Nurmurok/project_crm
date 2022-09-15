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

    FilterByUserid
)

urlpatterns = [
    path('list/', ProductListApiView.as_view(), name='prod-list'),
    path('create/', ProductCreateApiView.as_view(), name='prod-create'),
    path('detail/<int:id>/', ProductDetailApiView.as_view(), name='detail'),
    path('update/<int:id>/', ProductUpdateApiView.as_view(), name='update'),
    path('delete/<int:id>/', ProductDestroyApiView.as_view(), name='delete'),
    path('category_list/', CategoryListApiView.as_view(), name='cat-list'),
    path('cat_create/', CategoryCreateApiView.as_view(), name='cat-create'),
    path('delete/category/<int:id>/', CategoryDestroyApiView.as_view(), name='cat-create'),
    #Filter by category and price(больше или равно)использовала Q
    path('filterByCategory/<slug:name>/<int:price>/', FilterByCategory.as_view(), name='filter'),
    path('filter_by_user_id/<int:id>/', FilterByUserid.as_view(), name='filter-username'),

]
from django.urls import path 

from .views import ProductViwsSet, UserAPIView

urlpatterns = [
    path('products', ProductViwsSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('products/<str:pk>', ProductViwsSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('user', UserAPIView.as_view()),
]
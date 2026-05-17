from django.urls import path
from .views import hello_view, time_view, product_list

urlpatterns = [
    path('hello/', hello_view, name='hello'),
    path('time/', time_view, name='time'),
    path('products/', product_list, name='products'),
]

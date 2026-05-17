from django.urls import path
from .views import hello_view, time_view, product_list, add_product

urlpatterns = [
    path('hello/', hello_view, name='hello'),
    path('time/', time_view, name='time'),
    path('products/', product_list, name='products'),
    path('add/', add_product, name='add product')
]

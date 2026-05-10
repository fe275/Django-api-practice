from django.urls import path
from .views import hello_view, time_view

urlpatterns = [
    path('hello/', hello_view, name='hello'),
    path('time/', time_view, name='time'),
]

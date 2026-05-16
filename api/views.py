from django.http import JsonResponse
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer

# Create your views here.


def hello_view(request):
    return JsonResponse({'message': 'hello'})


def time_view(request):
    now = timezone.now()
    return JsonResponse({'time': str(now)})


@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

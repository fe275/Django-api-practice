from django.http import JsonResponse
from django.utils import timezone

# Create your views here.


def hello_view(request):
    return JsonResponse({'message': 'hello'})


def time_view(request):
    now = timezone.now()
    return JsonResponse({'time': str(now)})

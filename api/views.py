from django.http import JsonResponse

# Create your views here.


def hello_view(request):
    return JsonResponse({'message': 'hello'})

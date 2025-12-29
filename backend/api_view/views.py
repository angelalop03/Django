from django.http import JsonResponse
import json
# Create your views here.

#GETS
def hello_world(request, *args, **kwargs):
    body = "Hello, World!"
    return JsonResponse(body, status=200)


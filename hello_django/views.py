from django.http import JsonResponse
import json


def ping(request):
    data = {"ping": "pong!"}
    return JsonResponse(data)


def loanapp(request):
    data = json.loads(request.body.decode('utf-8'))
    return JsonResponse(data)

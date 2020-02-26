import json

from django.http import JsonResponse


def ping(request):
    data = {"ping": "pong!"}
    return JsonResponse(data)


def loanapp(request):
    data = json.loads(request.body.decode("utf-8"))
    return JsonResponse(data)

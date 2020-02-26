from django.http import JsonResponse


def ping(request):
    data = {"ping": "pong!"}
    return JsonResponse(data)


def loanapp(request):
    data = request.body
    return JsonResponse(data)

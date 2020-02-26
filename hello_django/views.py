import json

from django.http import JsonResponse
import json

from .models import Business, Owner


def ping(request):
    data = {"ping": "pong!"}
    return JsonResponse(data)


def loanapp(request):
<<<<<<< HEAD
    data = json.loads(request.body.decode("utf-8"))
    business_data = data["Business"]
    business_name = business_data["Name"]
    Business.objects.create(name=business_name, data=business_data)
    all_owner_data = data["Owners"]
    for entry in all_owner_data:
        owner_name = entry["Name"]
        Owner.objects.create(name=owner_name, data=entry)
=======
    data = json.loads(request.body.decode('utf-8'))
>>>>>>> dd1dd0a731b12dd8bfb6ae911a33085a3e8578e7
    return JsonResponse(data)

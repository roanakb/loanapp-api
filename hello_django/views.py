import json
import random

from django.http import JsonResponse

from loanapp.models import Business, Owner


def ping(request):
    data = {"ping": "pong!"}
    return JsonResponse(data)


def status(request):
    data = json.loads(request.body.decode("utf-8"))
    business = Business.objects.filter(data__CFRequestId=data["CFRequestId"])
    out = ""
    if len(business) > 0:
        val = random.uniform(0, 1)
        if val > 0.66:
            out = "2 Weeks until completion"
        elif val > 0.33:
            out = "Will be done tomorrow"
        else:
            out = "Application will be processed by April 11, 2063"
    else:
        out = "Invalid CFRequestId"
    output = {"Status": out}
    return JsonResponse(output)


def loanapp(request):
    data = json.loads(request.body.decode("utf-8"))
    business_data = {
        **data["Business"],
        **data["RequestHeader"],
        **data["CFApplicationData"],
    }
    business_name = business_data["Name"]
    business_repeats = Business.objects.filter(name=business_name)
    if len(business_repeats) > 0:
        existing_business = business_repeats[0]
        existing_business_data = existing_business.data
        for entry in business_data:
            value = business_data[entry]
            if not value:
                pass
            elif type(value) == type(data):
                for e in value:
                    inner_val = value[e]
                    if inner_val:
                        existing_business_data[entry][e] = inner_val
            else:
                existing_business_data[entry] = value
        existing_business.data = existing_business_data
        existing_business.save()
    else:
        Business.objects.create(name=business_name, data=business_data)
    all_owner_data = data["Owners"]
    for owner_dict in all_owner_data:
        owner_name = owner_dict["Name"]
        owner_repeats = Owner.objects.filter(name=owner_name)
        if len(owner_repeats) > 0:
            existing_owner = owner_repeats[0]
            existing_owner_data = existing_owner.data
            for entry in owner_dict:
                value = owner_dict[entry]
                if not value:
                    pass
                elif type(value) == type(data):
                    for e in value:
                        inner_val = value[e]
                        if inner_val:
                            existing_owner_data[entry][e] = inner_val
                else:
                    existing_owner_data[entry] = value
            existing_owner.data = existing_owner_data
            existing_owner.save()
        else:
            Owner.objects.create(
                name=owner_name, data=owner_dict, business=business_name
            )
    return JsonResponse(data)

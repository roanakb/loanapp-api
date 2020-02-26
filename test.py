import json

with open('sample.json') as json_file:
    data = json.load(json_file)
    business_data = data['Business']
    business_name = business_data['Name']
    #print(f'{business_name} and {business_data} ')
    all_owner_data = data['Owners']
    #print(all_owner_data)
    for owner_dict in all_owner_data:
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

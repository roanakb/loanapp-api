import json

with open('sample.json') as json_file:
    data = json.load(json_file)
    business_data = data['Business']
    business_name = business_data['Name']
    print(f'{business_name} and {business_data} ')
    all_owner_data = data['Owners']
    print(all_owner_data)
    for entry in all_owner_data:
        print(entry)

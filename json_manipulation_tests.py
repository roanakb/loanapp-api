import json

with open('sample.json') as json_file:
    data = json.load(json_file)
    business_data = data['Business']
    business_name = business_data['Name']
    #print(f'{business_name} and {business_data} ')
    all_owner_data = data['Owners']
    #print(all_owner_data)
    existing_owner_data = {
      "Name": "WH KennyTest",
      "FirstName": "WH",
      "LastName": "KennyTest",
      "Email": "whkennytest@caminofinancial.com",
      "HomeAddress": {
        "Address1": "5567 North Ridge Ct",
        "Address2": None,
        "City": "Berkeley",
        "State": "CA",
        "Zip": "94704"
      },
      "DateOfBirth": "1955-12-18T00:00:00",
      "HomePhone": "3451289776",
      "SSN": "435790261",
      "PercentageOfOwnership": 50.0
    }
    existing_business_data = {
      "Name": "Wow Inc",
      "SelfReportedCashFlow": {
        "AnnualRevenue": 49999999.0,
        "MonthlyAverageBankBalance": 94941.0,
        "MonthlyAverageCreditCardVolume": 18191.0
      },
      "Address": {
        "Address1": "1234 Red Ln",
        "Address2": "5678 Blue Rd",
        "City": "Santa Monica",
        "State": "CA",
        "Zip": "45321"
      },
      "TaxID": "839674398",
      "Phone": "6573248876",
      "NAICS": "79232",
      "HasBeenProfitable": True,
      "HasBankruptedInLast7Years": False,
      "InceptionDate": "2008-06-28T23:04:03.5507585+00:00"
    }
    if True:
        for owner_dict in all_owner_data:
            if owner_dict['Name'] == 'WH KennyTest':
                for entry in owner_dict:
                    value = owner_dict[entry]
                    if not value:
                        print(f'value = {value}')
                        pass
                    elif type(value) == type(data):
                        for e in value:
                            inner_val = value[e]
                            if inner_val:
                                existing_owner_data[entry][e] = inner_val
                                print(f'{entry} {e} {inner_val}')
                    else:
                        existing_owner_data[entry] = value
                        print(f'NOT DICT {entry} {value}')
        print(existing_owner_data)
    else:
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
        print(existing_business_data)

import requests
import json as json_lib
import math

url = "https://jlcpcb.com/api/overseas-pcb-order/v1/shoppingCart/smtGood/selectSmtComponentList/v2"

cookies = {
}

headers = {
    'accept': 'application/json, text/plain, */*',
}

# base_json_data = {
#     'pageSize': 25,
#     'componentLibraryType': None,
#     'stockFlag': None,
#     'stockSort': None,
#     'firstSortName': 'Resistors',
#     'secondSortName': 'Chip Resistor - Surface Mount',
#     'searchSource': 'search',
#     'searchType': 3,
#     'componentBrandList': [],
#     'componentSpecificationList': [],
#     'componentAttributeList': [],
#     'paramList': [],
#     'startStockNumber': None,
#     'firstSortId': 1,
#     'secondSortId': 2980,
#     'firstSortNameNew': 'Resistors',
#     'firstSortNameList': [],
#     'presaleTypes': [],
#     'componentLibTypes': ['base'],
#     'pcbAType': None,
# }

base_json_data = {"currentPage":1,"pageSize":25,"componentLibraryType":None,"stockFlag":None,"stockSort":None,"firstSortName":"Capacitors","secondSortName":"Multilayer Ceramic Capacitors MLCC - SMD/SMT","searchSource":"search","searchType":3,"componentBrandList":[],"componentSpecificationList":[],"componentAttributeList":[],"paramList":[],"startStockNumber":None,"firstSortId":2,"secondSortId":2929,"firstSortNameNew":"Capacitors","firstSortNameList":[],"presaleTypes":[],"componentLibTypes":["base"],"pcbAType":None}

# Make first request to get total count
json_data = base_json_data.copy()
json_data['currentPage'] = 1

response = requests.post(url, json=json_data)

if response.status_code == 200:
    first_response = response.json()
    total_count = first_response["data"]["componentPageInfo"]["total"]
    total_pages = math.ceil(total_count / 25)
    
    print(f"Total components: {total_count}")
    print(f"Total pages: {total_pages}")
    
    all_components = []
    
    # Fetch all pages
    for page in range(1, total_pages + 1):
        json_data = base_json_data.copy()
        json_data['currentPage'] = page
        
        print(f"Fetching page {page}/{total_pages}...")
        response = requests.post(url, json=json_data)
        
        if response.status_code == 200:
            data = response.json()
            components = data["data"]["componentPageInfo"]["list"]
            all_components.extend(components)
            print(f"  Got {len(components)} components")
        else:
            print(f"  Failed with status code: {response.status_code}")
    
    # Save all components to JSON
    with open('lcsc_data.json', 'w', encoding='utf-8') as f:
        json_lib.dump(all_components, f, indent=2, ensure_ascii=False)
    
    print(f"\nSuccess! Saved {len(all_components)} total components to lcsc_data.json")
else:
    print(f"Failed with status code: {response.status_code}")
    print(response.text)



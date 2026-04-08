import json
import csv
import os

# Load the LCSC data
json_file = os.path.join(os.path.dirname(__file__), '..', 'lcsc_data.json')

with open('lcsc_data.json', 'r', encoding='utf-8') as f:
    components = json.load(f)

# Prepare CSV output
csv_file = os.path.join(os.path.dirname(__file__), '..', 'lcsc_data.csv')

# Define CSV columns
fieldnames = ['componentCode', 'componentModelEn', 'erpComponentName', 'productBigImageAccessIdUrl', 
              'componentBrandEn', 'componentSpecificationEn', 'Capacitance', 'Tolerance', 'Voltage Rating']

with open('lcsc_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    for component in components:
        # Extract attributes
        attributes = {}
        if 'attributes' in component:
            for attr in component['attributes']:
                attr_name = attr.get('attribute_name_en', '')
                attr_value = attr.get('attribute_value_name', '')
                attributes[attr_name] = attr_value
        
        # Create row
        row = {
            'componentCode': component.get('componentCode', ''),
            'componentModelEn': component.get('componentModelEn', ''),
            'erpComponentName': component.get('erpComponentName', ''),
            'productBigImageAccessIdUrl': component.get('productBigImageAccessIdUrl', ''),
            'componentBrandEn': component.get('componentBrandEn', ''),
            'componentSpecificationEn': component.get('componentSpecificationEn', ''),
            'Capacitance': attributes.get('Capacitance', ''),
            'Tolerance': attributes.get('Tolerance', ''),
            'Voltage Rating': attributes.get('Voltage Rating', '')
        }
        
        writer.writerow(row)

print(f"Success! Wrote {len(components)} components to lcsc_data.csv")

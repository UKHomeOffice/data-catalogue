import sys
import ckanapi
import csv
import re
import os
import json

def create_id(name):
    removelist = ' '
    tidied = re.sub(r'[^\w'+removelist+']', '',name.lower())
    return '-'.join(re.findall('\"[^\"]*\"|\S+', tidied))

def create_tags(tags):
    return [{'name':x.strip()} for x in tags.split(',') if x!='']

def create_labels(tags):
    return [x.strip() for x in tags.split(',') if x!='']

def labels_to_values(field, labels):
    return [choice['value'] for choice in field['choices'] if choice['label'] in labels]

#Load schema from somewhere?
def load_schema():
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'ckan/plugins/ckanext-additional_fields/ckanext/additional_fields', 'schema.json')) as data_file:
        data = json.load(data_file)
        return { field['field_name']:field for field in data['dataset_fields'] }



if(len(sys.argv)) != 3:
    print """USAGE:
    python loader.py [serviceLocation] [apikey]"""
    sys.exit()

service_location = sys.argv[1]
api_key = sys.argv[2]
csv_location = 'formatted-examples.csv'

service = ckanapi.RemoteCKAN(service_location,
    user_agent='ckanapiexample/1.0 (+http://example.com/my/website)',
    apikey=api_key
)


print 'Creating Organisation'
try:
    service.action.organization_create(
        name='home-office',
        title='Home Office (HO)'
    )
except:
    pass

print 'Using schema'
schema = load_schema()

print 'Loading Datasets'
with open(csv_location, 'rb') as csvfile:
    csvreader = csv.DictReader(csvfile,
        delimiter=',',
        fieldnames=['Database Columns','name','summary','homeOfficeControlled','registry','informationAssetOwner','businessArea','type','currentUsers','policyConstraints','processForAccessing']
    )
    for row in csvreader:
        id=create_id(row['name'])
        print '  ' + id
        service.action.package_create(
            name=id,
            title=row['name'],
            owner_org='home-office',
            tags=create_tags(row['businessArea']),
            notes=row['summary'],
            business_area=labels_to_values(schema['business_area'], create_labels(row['businessArea']))
        )

print 'Finished'
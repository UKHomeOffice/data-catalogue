import json
import logging
import os
import re
import sys
import inflection
import uuid

import ckanapi
from openpyxl import load_workbook


def create_id(name):
    return inflection.parameterize(name)


def label_to_value(field, label):
    if not label == None:
        sanitised_label = label.replace(u'\xa0', u' ').strip()

        for choice in field['choices']:
            if choice['label'] == sanitised_label:
                return choice['value']

        raise Exception("Label not found in field", sanitised_label)


# Load schema from somewhere?
def load_schema():
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..',
                           'ckan/plugins/ckanext-additional_fields/ckanext/additional_fields',
                           'schema.json')) as data_file:
        data = json.load(data_file)
        return {field['field_name']: field for field in data['dataset_fields']}


if (len(sys.argv)) != 4:
    print """USAGE:
    python loader.py [serviceLocation] [apikey] [imputXlsDir]"""
    sys.exit()

service_location = sys.argv[1]
api_key = sys.argv[2]
input_xls_directory = sys.argv[3]
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
for file_name in os.listdir(input_xls_directory):
    full_path = os.path.join(input_xls_directory, file_name)

    if os.path.isdir(full_path) or not file_name.endswith(".xlsx"):
        continue

    workbook = load_workbook(full_path)
    sheet = workbook.active

    if not sheet['F2'].value == None:
        id = create_id(sheet['F2'].value)[:100]
    else:
        id = str(uuid.uuid4())

    try:
        print '  ' + id
        service.action.package_create(
            name=id,
            title=sheet['F2'].value,
            owner_org='home-office',
            summary=sheet['F2'].value,
            business_area=[label_to_value(schema['business_area'],
                                         sheet['F8'].value)],
            dataset_type=label_to_value(schema['dataset_type'],
                                        sheet['F9'].value),
            security_classification=label_to_value(schema['security_classification'],
                                                   sheet['F10'].value),
            can_be_public=label_to_value(schema['can_be_public'],
                                         sheet['F11'].value),
            contains_personal_information=label_to_value(schema['contains_personal_information'],
                                                         sheet['F12'].value),
            other_data_sources_feeding_in=sheet['F13'].value,
            data_originates_in_ho=label_to_value(schema['data_originates_in_ho'],
                                                 sheet['F14'].value),
            ho_responsible=label_to_value(schema['ho_responsible'],
                                          sheet['F15'].value),
            register=label_to_value(schema['register'],
                                    sheet['F16'].value),
            used_in_official_statistics=label_to_value(schema['used_in_official_statistics'],
                                                       sheet['F17'].value),
            how_the_data_can_be_used_any_policy_and_legal_constraints=sheet['F18'].value
        )
    except Exception, e:
        logging.error(e, exc_info=True)
        print id + ' failed'
        pass

print 'Finished'

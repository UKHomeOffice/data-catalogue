import json
import logging
import os
import pprint
import sys
import uuid

import ckanapi
import inflection
from openpyxl import load_workbook


def create_id(name):
    return inflection.parameterize(name)


def label_to_value(field, label):
    if not label == None:
        sanitised_label = label.replace(u'\xa0', u' ').strip()

        for choice in field['choices']:
            if choice['label'] == sanitised_label:
                return choice['value']

        return ""

        # raise Exception("Label not found in field", sanitised_label)


# Load schema from somewhere?
def load_schema():
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..',
                           'ckan/plugins/ckanext-additional_fields/ckanext/additional_fields',
                           'schema.json')) as data_file:
        data = json.load(data_file)
        return {field['field_name']: field for field in data['dataset_fields']}


if (len(sys.argv)) != 4:
    print """USAGE:
    python loader.py [serviceLocation] [apikey] [inputXls]"""
    sys.exit()

service_location = sys.argv[1]
api_key = sys.argv[2]
input_xls = sys.argv[3]

service = ckanapi.RemoteCKAN(service_location,
                             user_agent='ckanapiexample/1.0 (+http://example.com/my/website)',
                             apikey=api_key
                             )

print 'Using schema'
schema = load_schema()

print 'Loading Datasets'

workbook = load_workbook(input_xls)
sheet = workbook.active

for row in range(3, sheet.max_row):
#for row in range(3, 126):

    organisation = "Unknown"
    if sheet.cell(row=row, column=7).value:
        organisationList = sheet.cell(row=row, column=7).value
    #can be a list of organisations
    organisations = organisationList.split(',');
    
    for org in organisations:
        pprint.pprint(org)

        print 'Creating Organisation'
        try:
            service.action.organization_create(
                name=org.strip().lower().replace(' ', '-'),
                title=org
            )
        except:
            pass

    title = "????"

    if sheet.cell(row=row, column=2).value:
        id = create_id(sheet.cell(row=row, column=2).value)[:100]
        title = sheet.cell(row=row, column=2).value
    else:
        continue

    businessAreaList = sheet.cell(row=row, column=9).value

    businessAreaArray = businessAreaList.split(',');
    baValueArray = []

    for ba in businessAreaArray:
        baValueArray.append(label_to_value(schema['business_area'],ba.strip()))
        
    try:
        pprint.pprint( " -- " + organisations[0] + " -- " + organisations[0].lower().replace(' ', '-'))

        pprint.pprint( " -- id -- " + id)
        pprint.pprint( " -- title -- " + title)
        pprint.pprint( " -- sheet.cell(row=row, column=3).value -- " + sheet.cell(row=row, column=3).value)
        pprint.pprint( " -- sheet.cell(row=row, column=15).value -- " + sheet.cell(row=row, column=15).value)
        pprint.pprint( " -- sheet.cell(row=row, column=4).value -- " + sheet.cell(row=row, column=4).value)
        pprint.pprint( " -- sheet.cell(row=row, column=10).value -- " + sheet.cell(row=row, column=10).value)
	ho_responsible=label_to_value(schema['ho_responsible'],
                                              sheet.cell(row=row, column=4).value)
	pprint.pprint("ho_responsible " + ho_responsible)
        pprint.pprint("sheet.cell(row=row, column=18).value " + sheet.cell(row=row, column=18).value)
        pprint.pprint("baValueArray: ")
        pprint.pprint(baValueArray)


        print '  ' + id
        service.action.package_create(
                name=id,
               title=title,
               owner_org=organisations[0].strip().lower().replace(' ', '-'),
               summary=sheet.cell(row=row, column=3).value,
                 dataset_type=[label_to_value(schema['dataset_type'],
                                            sheet.cell(row=row, column=8).value)],
               security_classification=sheet.cell(row=row, column=15).value.lower(),
               ho_responsible=label_to_value(schema['ho_responsible'],
                                              sheet.cell(row=row, column=4).value),
               register=label_to_value(schema['register'],
                                        sheet.cell(row=row, column=4).value),
#               how_the_data_can_be_used_any_policy_and_legal_constraints=sheet.cell(row=row, column=10).value,
#               business_area=["criminal_policing_group", "border_force"],
               business_area=baValueArray,
               api_url=sheet.cell(row=row, column=18).value,
               description=sheet.cell(row=row, column=19).value,
               can_be_public=label_to_value(schema['can_be_public'],
                                        sheet.cell(row=row, column=16).value),
               used_in_official_statistics=label_to_value(schema['used_in_official_statistics'],
                                        sheet.cell(row=row, column=17).value),
               how_the_data_can_be_used_any_policy_and_legal_constraints=sheet.cell(row=row,column=10).value)

    except Exception, e:
        logging.error(e, exc_info=True)
        print id + ' failed'
    pass

print 'Finished'

import json
import os

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class Additional_FieldsPlugin(plugins.SingletonPlugin, toolkit.DefaultDatasetForm):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IFacets)
    plugins.implements(plugins.IPackageController, inherit=True)

    def update_config(self, config):
        toolkit.add_template_directory(config, 'templates')

    # IFacet interface
    def dataset_facets(self, facets_dict, package_type):
        facets_dict['vocab_category'] = toolkit._('Category')
        facets_dict['security_classification'] = toolkit._('Security Classification')
        facets_dict['contains_personal_information'] = toolkit._('Contains Personal Data')

        return facets_dict

    def group_facets(self, facets_dict, group_type, package_type):
        facets_dict['vocab_category'] = toolkit._('Category')
        facets_dict['security_classification'] = toolkit._('Security Classification')
        facets_dict['contains_personal_information'] = toolkit._('Contains Personal Data')

        return facets_dict

    def organization_facets(self, facets_dict, organization_type, package_type):
        facets_dict['vocab_category'] = toolkit._('Category')
        facets_dict['security_classification'] = toolkit._('Security Classification')
        facets_dict['contains_personal_information'] = toolkit._('Contains Personal Data')

        return facets_dict

    def before_index(self, pkg_dict):
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                               'schema.json')) as data_file:
            data = json.load(data_file)
            for dataset in data['dataset_fields']:

                if dataset['field_name'] in ['category'] and 'extras_' + \
                        dataset['field_name'] in pkg_dict:
                    multi_value_field_value = self.parse_multi_value(
                        pkg_dict['extras_' + dataset['field_name']])
                    pkg_dict['vocab_' + dataset['field_name']] = [self.map_to_label(dataset, value)
                                                                  for value
                                                                  in multi_value_field_value]

                if dataset['field_name'] in ['security_classification',
                                             'contains_personal_information'] and 'extras_' + \
                        dataset['field_name'] in pkg_dict:
                    field_value = pkg_dict['extras_' + dataset['field_name']]
                    pkg_dict['vocab_' + dataset['field_name']] = [field_value]

        return pkg_dict

    def map_to_label(self, definition, value):
        matching = value

        for d in definition['choices']:
            if d['value'] == value:
                matching = d['label']

        return matching

    def parse_multi_value(self, value):
        try:
            return json.loads(value)
        except ValueError:
            return [value]

    def is_fallback(self):
        return True

    def package_types(self):
        return []

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import json
import os

from homeoffice.datacatalogue.auth_middleware import DCAuthMiddleware

class Datacatalogue_ThemePlugin(plugins.SingletonPlugin, toolkit.DefaultDatasetForm):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IFacets)
    plugins.implements(plugins.IPackageController, inherit=True)
    plugins.implements(plugins.IMiddleware)
    plugins.implements(plugins.IRoutes)

    # IConfigurer
    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'datacatalogue_theme')

    # IMiddleware
    def make_middleware(self, app, config):
        app = DCAuthMiddleware(app)
        return app


    #IFacet interface

    def dataset_facets(self, facets_dict, package_type):
        facets_dict['vocab_business_area'] = toolkit._('Business areas')
        facets_dict['security_classification'] = toolkit._('Security Classification')
        return facets_dict

    def group_facets(self, facets_dict, group_type, package_type):
        facets_dict['vocab_business_area'] = toolkit._('Business areas')
        facets_dict['security_classification'] = toolkit._('Security Classification')
        return facets_dict

    def organization_facets(self, facets_dict, organization_type, package_type):
        facets_dict['vocab_business_area'] = toolkit._('Business areas')
        facets_dict['security_classification'] = toolkit._('Security Classification')
        return facets_dict

    def before_index(self, pkg_dict):
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'schema.json')) as data_file:
            data = json.load(data_file)
            for dataset in data['dataset_fields']:
                if dataset['field_name'] == 'business_area' and 'extras_business_area' in pkg_dict:
                    ba = self.parse_multi_value(pkg_dict['extras_business_area'])
                    pkg_dict['vocab_business_area'] = [self.map_to_label(dataset, value) for value in ba]
        return pkg_dict

    def map_to_label(self, definition, value):
        matching = [d['label'] for d in definition['choices'] if d['value'] == value]
        return (matching or [value])[0]

    def parse_multi_value(self, value):
        try:
            return json.loads(value)
        except ValueError:
            return [value]


    def is_fallback(self):
        return True

    def package_types(self):
        return []

    # healthcheck endpoint

    def before_map(self, map):
        return map

    def after_map(self, map):
        controller = 'ckanext.datacatalogue_theme.controller:CustomController'
        map.connect('healthcheck', '/healthcheck',
                controller=controller, action='healthcheck')
        return map
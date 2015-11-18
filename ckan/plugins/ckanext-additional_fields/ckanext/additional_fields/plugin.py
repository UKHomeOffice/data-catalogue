import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import json

class Additional_FieldsPlugin(plugins.SingletonPlugin, toolkit.DefaultDatasetForm):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IFacets)
    plugins.implements(plugins.IPackageController, inherit=True)

    def update_config(self, config):
        toolkit.add_template_directory(config, 'templates')


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
        if 'extras_business_area' in pkg_dict:
            ba = self.parse_multi_value(pkg_dict['extras_business_area'])
            pkg_dict['vocab_business_area'] = ba
        return pkg_dict

    def parse_multi_value(self, value):
        try:
            return json.loads(value)
        except ValueError:
            return [value]


    def is_fallback(self):
        return True

    def package_types(self):
        return []
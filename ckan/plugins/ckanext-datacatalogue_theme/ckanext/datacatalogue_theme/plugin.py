import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import json
import os
import pylons.config as config

from homeoffice.datacatalogue.auth_middleware import DCAuthMiddleware


def get_version_number():
    value = os.environ.get("DC_VERSION", None)
    if value is None:
        value = "DC_VERSION env variable not set"
    return value

def get_facets():
    facetsList = config.get(
        'ckan.datacatalogue.search_facets', 'organization tags')
    return facetsList.split()



class Datacatalogue_ThemePlugin(plugins.SingletonPlugin, toolkit.DefaultDatasetForm):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IFacets)
    plugins.implements(plugins.IPackageController, inherit=True)
    plugins.implements(plugins.IMiddleware)
    plugins.implements(plugins.IRoutes)
    plugins.implements(plugins.ITemplateHelpers)

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
        return facets_dict

    def group_facets(self, facets_dict, group_type, package_type):
        return facets_dict

    def organization_facets(self, facets_dict, organization_type, package_type):
        #hide facets on orgs
        facets_dict.clear()
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
        map.connect('home', '/', controller='package', action='search')
        return map

    def after_map(self, map):
        controller = 'ckanext.datacatalogue_theme.controller:CustomController'
        map.connect('healthcheck', '/healthcheck',
                controller=controller, action='healthcheck')
        return map
    
    def get_helpers(self):
        return {'datacatalogue_theme_get_version_number': get_version_number,
                'datacatalogue_theme_get_facets': get_facets,
            }



class Datacatalogue_DBPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurable)
    def configure(self, config):
        database_user = os.environ.get("DATABASE_USER", None)
        database_password = os.environ.get("DATABASE_PASSWORD", None)
        database_host = os.environ.get("DATABASE_HOST", None)
        database_port = os.environ.get("DATABASE_PORT", None)
        if database_user is None or database_password is None or database_host is None:
            return
        if database_port is None:
            #use the default
            database_port = "5432"

        url = "postgres://"
        url += database_user
        url += ":"
        url += database_password
        url += "@"
        url += database_host
        url += ":"
        url += database_port
        url += "/ckan"

        config['sqlalchemy.url'] = url
        print("Setting database " + database_host + ":" + database_port)

        #read in solr basic auth config
        print("Talking to solr on " + config['solr_url'])

        solr_user = os.environ.get("SOLR_USER", None)
        if(solr_user is not None):
            config['solr_user'] =solr_user
            print("with the user " + config['solr_user'])

        solr_password = os.environ.get("SOLR_PASSWORD", None)
        if(solr_password is not None):
            config['solr_password'] = solr_password
            print("solr password " + config['solr_password'])

    def readCreds(self, creds):
        if(creds is None or ":" not in creds or creds == ":"):
            return []
        name_and_password = creds.split(":")
        
        name_and_password[0] = name_and_password[0].strip()
        name_and_password[1] = name_and_password[1].strip()
        return name_and_password

    def read_creds_file(self, creds_file):
        creds_string = ""
        with open(creds_file, 'r') as f:
            creds_string = f.readline()
        return creds_string.strip()






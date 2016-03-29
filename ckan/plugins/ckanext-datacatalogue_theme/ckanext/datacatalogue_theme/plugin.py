import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

from homeoffice.datacatalogue.auth_middleware import DCAuthMiddleware

class Datacatalogue_ThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IMiddleware)

    # IConfigurer
    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'datacatalogue_theme')


    # IMiddleware
    def make_middleware(self, app, config):
        app = DCAuthMiddleware(app)
        return app


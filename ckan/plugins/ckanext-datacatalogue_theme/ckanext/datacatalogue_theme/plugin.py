import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

non_auth_list = ['/user/login', '/user/register', '/user/reset']

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
        app = Middleware(app)
        return app

class Middleware(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
	if environ.get('REMOTE_USER') is None:
	    if environ.get('PATH_INFO') in non_auth_list:
	        return self.app(environ, start_response)
	    else:
	        start_response('401', [('Location', 'user/login')])
	        return []
	else:
	    return self.app(environ, start_response)
        s

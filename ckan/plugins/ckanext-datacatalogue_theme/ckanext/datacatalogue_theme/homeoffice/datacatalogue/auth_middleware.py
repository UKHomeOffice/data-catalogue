# /ckan/plugins/ckanext-datacatalogue_theme/ckanext/datacatalogue_theme/plugin.py
import logging

log = logging.getLogger(__name__)

non_auth_list = ['/user/login', '/user/register', '/user/reset', '/healthcheck', '/user/logged_out']

class DCAuthMiddleware(object):
    def __init__(self, app):
        self.app = app
    def __call__(self, environ, start_response):
        if self.checkUser(environ):
            return self.app(environ, start_response)
        else:
            start_response('401', [('Location', 'user/login')])
            return []
    #Check if there is a user or an api key in the headers, or if it is one of the 
    #non-auth pages
    def checkUser(self, environ):
        if environ.get('REMOTE_USER') is None and environ.get('HTTP_X_CKAN_API_KEY') is None:
            if environ.get('PATH_INFO') is not None and environ.get('PATH_INFO').lower().startswith(tuple(non_auth_list)):
                return True
            else:
                return False
        else:
            return True

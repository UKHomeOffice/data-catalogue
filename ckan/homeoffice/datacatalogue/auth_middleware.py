# /ckan/plugins/ckanext-datacatalogue_theme/ckanext/datacatalogue_theme/plugin.py

non_auth_list = ['/user/login', '/user/register', '/user/reset']

class DCAuthMiddleware(object):
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

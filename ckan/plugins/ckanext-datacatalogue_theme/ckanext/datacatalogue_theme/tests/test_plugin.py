"""Tests for plugin.py."""
import ckanext.datacatalogue_theme.plugin as plugin
import pylons.test
import paste.fixture
import logging
import os
from ckanext.datacatalogue_theme.homeoffice.datacatalogue.auth_middleware import DCAuthMiddleware


log = logging.getLogger(__name__)

def test_plugin():
    pass

class TestAuthorizationPlugin(object):
    def test_no_username(self):
        self.app = paste.fixture.TestApp(pylons.test.pylonsapp)
        middleware = DCAuthMiddleware(self.app)
        check = middleware.checkUser(os.environ)
        assert check == False

    def test_with_username(self):
        self.app = paste.fixture.TestApp(pylons.test.pylonsapp)
        middleware = DCAuthMiddleware(self.app)
        os.environ['REMOTE_USER'] = 'chris'
        check = middleware.checkUser(os.environ)
        assert check == True

    def test_no_username_login_page(self):
        self.app = paste.fixture.TestApp(pylons.test.pylonsapp)
        middleware = DCAuthMiddleware(self.app)
        os.environ['PATH_INFO'] = '/user/login'
        check = middleware.checkUser(os.environ)
        assert check == True

    def test_no_username_register_page(self):
        self.app = paste.fixture.TestApp(pylons.test.pylonsapp)
        middleware = DCAuthMiddleware(self.app)
        os.environ['PATH_INFO'] = '/user/register'
        check = middleware.checkUser(os.environ)
        assert check == True

    def test_no_username_reset_page(self):
        self.app = paste.fixture.TestApp(pylons.test.pylonsapp)
        middleware = DCAuthMiddleware(self.app)
        os.environ['PATH_INFO'] = '/user/reset'
        check = middleware.checkUser(os.environ)
        assert check == True

    def test_no_username_reset_page_with_key(self):
        self.app = paste.fixture.TestApp(pylons.test.pylonsapp)
        middleware = DCAuthMiddleware(self.app)
        os.environ['PATH_INFO'] = '/user/reset/ebe0c59e-5d27-4331-8a7c-17ead7ac7f38?key=d1d7a7df0a'
        check = middleware.checkUser(os.environ)
        assert check == True

    def test_with_api_key(self):
        self.app = paste.fixture.TestApp(pylons.test.pylonsapp)
        middleware = DCAuthMiddleware(self.app)
        os.environ['HTTP_X_CKAN_API_KEY'] = 'aaaa'
        check = middleware.checkUser(os.environ)
        assert check == True

    def teardown(self):
        log.debug('tearing it down')
        if 'HTTP_X_CKAN_API_KEY' in os.environ:
            del os.environ['HTTP_X_CKAN_API_KEY']
        if 'PATH_INFO' in os.environ:
            del os.environ['PATH_INFO']
        if 'REMOTE_USER' in os.environ:
            del os.environ['REMOTE_USER']



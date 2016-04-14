import ckan.lib.base as base

class CustomController(base.BaseController):

    def healthcheck(self):


        return {'healthcheck OK'}


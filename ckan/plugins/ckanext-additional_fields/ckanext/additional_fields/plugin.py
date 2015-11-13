import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

class Additional_FieldsPlugin(plugins.SingletonPlugin, toolkit.DefaultDatasetForm):
    plugins.implements(plugins.IDatasetForm)
    plugins.implements(plugins.IConfigurer)

    def update_config(self, config):
        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        toolkit.add_template_directory(config, 'templates')

    def create_package_schema(self):
        schema = super(Additional_FieldsPlugin, self).create_package_schema()
        schema.update({
            'security_classification': [toolkit.get_validator('ignore_missing'),
                                        toolkit.get_converter('convert_to_extras')]

        })
        return schema

    def update_package_schema(self):
        schema = super(Additional_FieldsPlugin, self).update_package_schema()
        schema.update({
            'security_classification': [toolkit.get_validator('ignore_missing'),
                                        toolkit.get_converter('convert_to_extras')]
        })
        return schema

    def show_package_schema(self):
        schema = super(Additional_FieldsPlugin, self).show_package_schema()
        schema.update({
            'security_classification': [toolkit.get_converter('convert_from_extras'),
                                        toolkit.get_validator('ignore_missing')]
        })
        return schema

    def is_fallback(self):
        # Return True to register this plugin as the default handler for
        # package types not handled by any other IDatasetForm plugin.
        return True

    def package_types(self):
        # This plugin doesn't handle any special package types, it just
        # registers itself as the default (above).
        return []
import pylons.test
from nose.tools import *
import ckanext.datacatalogue_theme.plugin as plugin

import logging

log = logging.getLogger(__name__)

def test_uploader_true():
    passResult = "Everything ok : true"
    answer = passResult[16:].strip()
    assert answer == "true"
    pass


def test_uploader_false():
    passResult = "Everything ok : false"
    answer = passResult[16:].strip()
    assert answer == "false"
    pass



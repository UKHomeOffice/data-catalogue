from nose.tools import *
from ckanext.datacatalogue_theme.homeoffice.datacatalogue.clamav_client import ClamAVClient as client

def test_scan:
    assert client.scan_file("testfile") == True

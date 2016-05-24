import pylons.test
import logging
import loader_util

log = logging.getLogger(__name__)
entry = "type: Information Asset Owner\nname: Chris Davidson\nemail: chris.davidson@homeoffice.gsi.gov.uk"

def test_getName():    
    name = loader_util.getIAOName(entry)
    log.debug(name)
    assert "Chris Davidson" == name

def test_getJustName():    
    name = loader_util.getIAOName("Chris Davidson")
    log.debug(name)
    assert "Chris Davidson" == name


def test_getEmail():
    email = loader_util.getIAOEmail(entry)
    log.debug(email)
    assert "chris.davidson@homeoffice.gsi.gov.uk" == email

def test_getEmailFromJustName():
    email = loader_util.getIAOEmail("Chris Davidson")
    log.debug(email)
    assert "" == email

def test_ShortDescription():
    desc = "a short description."
    summary = loader_util.createSummary(desc)
    assert "a short description." == summary

def test_LongDescription():
    desc = "a very long description with lots of words. a very long description with lots of words. a very long description with lots of words. a very long description with lots of words. a very long description with lots of words. "
    summary = loader_util.createSummary(desc)
    assert "a very long description with lots of words. a very long description with lots of words. a very long description with lots of words. a very long description with lots of words." == summary

def test_LongDescriptionNoStops():
    desc = "a very long description with lots of words a very long description with lots of words a very long description with lots of words a very long description with lots of words a very long description with lots of words "
    summary = loader_util.createSummary(desc)
    assert "a very long description with lots of words a very long description with lots of words a very long description with lots of words a very long description with lots of words a very l" == summary


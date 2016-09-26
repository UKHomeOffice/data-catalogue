import pylons.test
import re
from nose.tools import *

import logging

log = logging.getLogger(__name__)

lower_regex = "[a-z]"
upper_regex = "[A-Z]"
number_regex = "[0-9]"
special_regex = "[!@#$%&*()+\-{}^?<>_]"

def test_special_chars_zero():
    password = "0000"
    assert not re.search(special_regex, password)
    pass

def test_special_chars_cap():
    password = "PPPPP"
    assert not re.search(special_regex, password)
    pass

def test_special_chars_lower():
    password = "assword"
    assert not re.search(special_regex, password)
    pass

def test_special_chars_exclamation():
    password = "!!!!!"
    assert re.search(special_regex, password)
    pass

def test_special_chars_at():
    password = "@@@@"
    assert re.search(special_regex, password)
    pass

def test_special_chars_hash():
    password = "#####"
    assert re.search(special_regex, password)
    pass

def test_special_chars_dollar():
    password = "$$$$$"
    assert re.search(special_regex, password)
    pass

def test_special_chars_exclamation():
    password = "!!!!!"
    assert re.search(special_regex, password)
    pass

def test_special_chars_percent():
    password = "%%%%%"
    assert re.search(special_regex, password)
    pass

def test_special_chars_caret():
    password = "^^^^"
    assert re.search(special_regex, password)
    pass

def test_special_chars_ampersand():
    password = "&&&&&"
    assert re.search(special_regex, password)
    pass

def test_special_chars_star():
    password = "****"
    assert re.search(special_regex, password)
    pass

def test_special_chars_open():
    password = "(((("
    assert re.search(special_regex, password)
    pass

def test_special_chars_close():
    password = ")))))"
    assert re.search(special_regex, password)
    pass

def test_special_chars_underline():
    password = "_____"
    assert re.search(special_regex, password)
    pass

def test_special_chars_hypen():
    password = "------"
    assert re.search(special_regex, password)
    pass

def test_special_chars_equals():
    password = "++++++"
    assert re.search(special_regex, password)
    pass

def test_special_chars_plus():
    password = "++++++"
    assert re.search(special_regex, password)
    pass

def test_special_chars_question():
    password = "??????"
    assert re.search(special_regex, password)
    pass

def test_special_chars_open_angle():
    password = "<<<<<"
    assert re.search(special_regex, password)
    pass

def test_special_chars_close_angle():
    password = ">>>>>"
    assert re.search(special_regex, password)
    pass
def test_special_chars_only():
    password = "%^$#(+*)!@-{}"
    assert re.search(special_regex, password)
    pass


def test_length_short():
    password = "passwor"
    assert not search_password(password)
    pass

def test_length_exact():
    password = "Passwo1$"
    assert search_password(password)
    pass

def test_lowercase_only():
    password = "password"
    assert re.search(lower_regex, password)
    pass

def test_uppercase_only():
    password = "PASSWORD"
    assert re.search(upper_regex, password)
    pass

def test_numbers_only():
    password = "12345678"
    assert re.search(number_regex, password)
    pass


def test_lowercase_and_uppercase_only():
    password = "passWORD"
    assert not search_password(password)
    pass

def test_lower_upper_number_only():
    password = "Passw0rd"
    assert not search_password(password)
    pass

def test_lowercase_and_uppercase_only():
    password = "passWORD"
    assert not search_password(password)
    pass

def test_lower_upper_number_only():
    password = "Passw0rd"
    assert not search_password(password)
    pass

def test_pass():
    password = "Passw0rd%"
    assert search_password(password)
    pass

def search_password(password):
    if len(password) < 8:
        return False
    elif re.search(lower_regex, password) is None:
        return False
    elif re.search(upper_regex, password) is None:
        return False
    elif re.search(number_regex, password) is None:
        return False
    elif re.search(special_regex, password) is None:
        return False
    else:
        return True


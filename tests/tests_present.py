import pytest 
from lib.present import *

def test_present():
    present = Present()
    with pytest.raises(Exception) as e:
        present.wrap()
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."

def test_to_wrap():
    present = Present()
    present.wrap(90)
    assert present.unwrap == 90 

from lib.report_length import *

def test_report_length():
    result = report_length("supercalifraglisticexpalidious")
    assert result == "This string was 30 characters long."

def test_report_length():
    result = report_length("Reeva is the best")
    assert result == "This string was 17 characters long."
from lib.string_builder import *

def test_string_builder():
    string_builder = StringBuilder()
    string_builder.add("yessir")
    result = string_builder.size()
    assert result == 6
    result = string_builder.output()
    assert result == "yessir"

def test_string_builder():
    string_builder = StringBuilder()
    string_builder.add("woooooooooooop")
    result = string_builder.size()
    assert result == 14
    result = string_builder.output()
    assert result == "woooooooooooop"



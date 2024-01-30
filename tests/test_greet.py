from lib.greet import *

def test_greet():
    result = greet("Reeva")
    assert result == "Hello, Reeva!"

from lib.counter import *

def test_counts_number():
    counter = Counter()
    counter.add(20)
    result = counter.report()
    assert result == "Counted to 20 so far."


def test_counts_number():
    counter = Counter()
    counter.add(40)
    result = counter.report()
    assert result == "Counted to 40 so far."

def test_counts_number():
    counter = Counter()
    counter.add(100)
    result = counter.report()
    assert result == "Counted to 100 so far."
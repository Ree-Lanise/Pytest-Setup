from lib.gratitudes import *

def test_giving_gratitudes():
    gratitude = Gratitudes()
    gratitude.add("waking up this morning")
    result = gratitude.format()
    assert result == "Be grateful for: waking up this morning"


def test_giving_gratitudes():
    gratitude = Gratitudes()
    gratitude.add("a good paying job")
    result = gratitude.format()
    assert result == "Be grateful for: a good paying job"
    


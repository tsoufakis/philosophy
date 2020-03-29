from philosophy import find_philosophy

def test_basic():
    # no italics, no parentheses
    assert find_philosophy('https://en.wikipedia.org/wiki/Object_of_the_mind') == ['https://en.wikipedia.org/wiki/Object_of_the_mind', 'https://en.wikipedia.org/wiki/Object_(philosophy)', 'https://en.wikipedia.org/wiki/Philosophy']

def test_parens():
    assert find_philosophy('https://en.wikipedia.org/wiki/Mathematics') == ['https://en.wikipedia.org/wiki/Mathematics', 'https://en.wikipedia.org/wiki/Quantity', 'https://en.wikipedia.org/wiki/Counting', 'https://en.wikipedia.org/wiki/Number', 'https://en.wikipedia.org/wiki/Mathematical_object', 'https://en.wikipedia.org/wiki/Abstract_object', 'https://en.wikipedia.org/wiki/Object_(philosophy)', 'https://en.wikipedia.org/wiki/Philosophy']

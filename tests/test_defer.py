import pytest
from py_token_stream import TokenStream


tokens = ['a', 'b', 'c', 'd']
token_stream = TokenStream(tokens)

def test_defer():
    assert token_stream.defer('z') == None

def test_peek():
    assert token_stream.peek() == 'z'

def test_lookahead_0():
    assert token_stream.lookahead(0) == 'z'

def test_lookahead_1():
    assert token_stream.lookahead(1) == 'a'

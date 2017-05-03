import pytest
from py_token_stream import TokenStream


tokens = ['a', 'b', 'c', 'd']
token_stream = TokenStream(tokens)

def test_advance():
    assert token_stream.advance() == 'a'

def test_peek():
    assert token_stream.peek() == 'b'

def test_lookahead_0():
    assert token_stream.lookahead(0) == 'b'

def test_lookahead_1():
    assert token_stream.lookahead(1) == 'c'

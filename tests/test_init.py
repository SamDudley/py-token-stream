import pytest
from py_token_stream import TokenStream


tokens = ['a', 'b', 'c', 'd']
token_stream = TokenStream(tokens)

def test_lookahead_index_error():
    with pytest.raises(IndexError):
        token_stream.lookahead(9)

def test_peek():
    assert token_stream.peek() == 'a'

def test_lookahead_0():
    assert token_stream.lookahead(0) == 'a'

def test_lookahead_1():
    assert token_stream.lookahead(1) == 'b'

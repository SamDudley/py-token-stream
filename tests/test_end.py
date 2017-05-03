import pytest
from py_token_stream import TokenStream


tokens = ['a', 'b', 'c', 'd']
token_stream = TokenStream(tokens)

def test_advance_1():
    assert token_stream.advance() == 'a'

def test_advance_2():
    assert token_stream.advance() == 'b'

def test_advance_3():
    assert token_stream.advance() == 'c'

def test_advance_4():
    assert token_stream.advance() == 'd'

def test_peek_index_error():
    with pytest.raises(IndexError):
        token_stream.peek()

def test_lookahead_0_index_error():
    with pytest.raises(IndexError):
        token_stream.lookahead(0)

def test_lookahead_1_index_error():
    with pytest.raises(IndexError):
        token_stream.lookahead(1)

def test_advance_index_error():
    with pytest.raises(IndexError):
        token_stream.advance()

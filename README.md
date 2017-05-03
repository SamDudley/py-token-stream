# py-token-stream

Take a list of tokens and produce a more useful API to give to a parser.

Inspired by [pugjs](https://github.com/pugjs)/[token-stream](https://github.com/pugjs/token-stream).

## Installation

    pip install py-token-stream

## Usage

```python
from py_token_stream import TokenStream

stream = TokenStream(['a', 'b', 'c', 'd'])

stream.peek()		# 'a'
stream.advance()	# 'a'
stream.lookahead(0)	# 'b'
stream.lookahead(1)	# 'c'
stream.advance()	# 'b'
stream.defer('z')
stream.peek()		# 'z'
stream.advance()	# 'z'
stream.advance()	# 'c'
stream.advance()	# 'd'
stream.advance()	# IndexError!
```

## API

### TokenStream.peek()

Gets and returns the next item in the stream without advancing the stream's position.

### TokenStream.advance()

Returns the next item in the stream and advances the stream by one item.

### TokenStream.lookahead(index)

Return the item at `index` position from the start of the stream, but don't advance the stream.  `TokenStream.lookahead(0)` is equivalent to `TokenStream.peek()`.

### TokenStream.defer(token)

Put a token on the start of the stream (useful if you need to back track after calling advance).

## License

    MIT

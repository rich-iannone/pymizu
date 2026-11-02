# ForeignPayloadError

A received payload in a language-private or unrecognized format: a peer sent outside the portable interchange subset. The message is consumed, never wedging the ring; the async drain rejects only the head waiter and continues.

Usage

``` python
ForeignPayloadError()
```

# Map

A staged, submitted map -- the handle-first return of

Usage

[Source](https://github.com/shikokuchuo/pymizu/blob/main/python/pymizu/_map.py#L1506-L2006)

``` python
Map(
    pool,
    plan,
)
```

[`Pool.map()`](../reference/Pool.map.md#pymizu.Pool.map) and [`PreparedMap.run()`](../reference/PreparedMap.md#pymizu.PreparedMap.run): collection happens exactly once, through the handle. `collect()` blocks; `collect_async()` / `await` resolves one asyncio Future when the results arrive (never on a streaming map -- its sliding task window advances in the blocking collect loop); `cancel()` stops the run: workers halt within about one batch and the outstanding tasks are cancelled. A dropped uncollected handle cancels at GC, so no run of fn is wasted. One collection per handle, as for tasks.

## Methods

| Name | Description |
|----|----|
| [cancel()](#cancel) | Stop the run: workers halt within about one batch and the |
| [collect()](#collect) | Block for the map's results; collect exactly once. |
| [collect_async()](#collect_async) | The event-driven collect: an asyncio.Future resolving with the |

### cancel()

Stop the run: workers halt within about one batch and the

Usage

[Source](https://github.com/shikokuchuo/pymizu/blob/main/python/pymizu/_map.py#L1968-L1988)

``` python
cancel()
```

outstanding tasks are cancelled. Advisory, as [`Task.cancel()`](../reference/Task.cancel.md#pymizu.Task.cancel): a queued task is skipped, a running batch completes and its result is dropped. A pending collect -- blocking or async -- ends with [`CancelledError`](../reference/CancelledError.md#pymizu.CancelledError). Safe to call more than once.

### collect()

Block for the map's results; collect exactly once.

Usage

[Source](https://github.com/shikokuchuo/pymizu/blob/main/python/pymizu/_map.py#L1875-L1903)

``` python
collect(timeout=None)
```

#### Parameters

`timeout: float | None = None`  
Seconds to wait for completion; None waits indefinitely. On expiry the outstanding work is cancelled and the `TIMEOUT` [`Sentinel`](../reference/Sentinel.md#pymizu.Sentinel) is returned, never raised.

#### Returns

`The results -- the same shapes and outcomes as`  
[`PreparedMap.run()`](../reference/PreparedMap.md#pymizu.PreparedMap) documents.

### collect_async()

The event-driven collect: an asyncio.Future resolving with the

Usage

[Source](https://github.com/shikokuchuo/pymizu/blob/main/python/pymizu/_map.py#L1905-L1937)

``` python
collect_async()
```

same results `collect()` returns (an element error rejects with its index) -- never blocks, never polls. Cancelling the Future detaches the waiter (the handle collects blocking again); it never cancels the map -- `cancel()` stays the explicit verb. A streaming map refuses: its sliding task window advances in the blocking collect loop.

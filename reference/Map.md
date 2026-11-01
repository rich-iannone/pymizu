# Map

A staged, submitted map; collects exactly once, through this handle.

Usage

[Source](https://github.com/shikokuchuo/pymizu/blob/main/python/pymizu/_map.py#L1506-L2011)

``` python
Map(
    pool,
    plan,
)
```

The handle-first return of [`Pool.map()`](../reference/Pool.map.md#pymizu.Pool.map) and [`PreparedMap.run()`](../reference/PreparedMap.md#pymizu.PreparedMap.run). `collect()` blocks; `collect_async()` / `await` resolves one asyncio Future when the results arrive (never on a streaming map -- its sliding task window advances in the blocking collect loop); `cancel()` stops the run: workers halt within about one batch and the outstanding tasks are cancelled. A dropped uncollected handle cancels at GC, so no run of fn is wasted. One collection per handle, as for tasks.

## Methods

| Name | Description |
|----|----|
| [cancel()](#cancel) | Stop the run: workers halt within about one batch. |
| [collect()](#collect) | Block for the map's results; collect exactly once. |
| [collect_async()](#collect_async) | Resolve one asyncio.Future with the results `collect()` returns. |

### cancel()

Stop the run: workers halt within about one batch.

Usage

[Source](https://github.com/shikokuchuo/pymizu/blob/main/python/pymizu/_map.py#L1971-L1993)

``` python
cancel()
```

Advisory, as [`Task.cancel()`](../reference/Task.cancel.md#pymizu.Task.cancel): the outstanding tasks are cancelled -- a queued task is skipped, a running batch completes and its result is dropped. A pending collect -- blocking or async -- ends with [`CancelledError`](../reference/CancelledError.md#pymizu.CancelledError). Safe to call more than once.

### collect()

Block for the map's results; collect exactly once.

Usage

[Source](https://github.com/shikokuchuo/pymizu/blob/main/python/pymizu/_map.py#L1876-L1904)

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

Resolve one asyncio.Future with the results `collect()` returns.

Usage

[Source](https://github.com/shikokuchuo/pymizu/blob/main/python/pymizu/_map.py#L1906-L1940)

``` python
collect_async()
```

The event-driven collect -- never blocks, never polls. An element error rejects with its index. Cancelling the Future detaches the waiter (the handle collects blocking again); it never cancels the map -- `cancel()` stays the explicit verb. A streaming map refuses: its sliding task window advances in the blocking collect loop.

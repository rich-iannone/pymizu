# Task.collect_async()

collect_async() -\> asyncio.Future

Usage

``` python
Task.collect_async()
```

The event-driven collect: an asyncio.Future that resolves with the task's result (or raises the error collect() raises) when the result arrives, without blocking or polling. Cancelling the Future detaches the waiter, so a later blocking collect() works again, and never cancels the task (only cancel() does).

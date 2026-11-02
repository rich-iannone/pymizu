# Task.cancel()

cancel() -\> bool

Usage

``` python
Task.cancel()
```

Advisory only, and never interrupts: a queued task is skipped, and a running one completes with its result dropped. Returns True when this call cancelled the task, False in every other case.

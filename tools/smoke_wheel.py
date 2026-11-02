"""Wheel smoke test, run by cibuildwheel's test-command.

Runs against the installed wheel with no repo code on sys.path: proves the
extension imports and the full spawn / stage / execute / publish / collect
path works from the wheel alone (workers are `python -m pymizu.worker` from
the same install).
"""

import pymizu

with pymizu.Pool.create(2) as pool:
    task = pool.submit(pow, 2, 16)
    result = task.collect(timeout=30)
    assert result == 65536, result

print(f"pymizu {pymizu.__version__}: pool round trip OK")

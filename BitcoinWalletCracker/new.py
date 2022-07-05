import functools, time


@functools.lru_cache(maxsize=12)
def slow_func(x):
    time.sleep(2)  # Simulate long computation
    yield x


@functools.lru_cache(maxsize=12)
def mamd(x):
    time.sleep(2)  # Simulate long computation
    yield x


print(slow_func(1))  # ... waiting for 2 sec before getting result
print(slow_func(1))  # ... waiting for 2 sec before getting result
  # already cached - result returned instantaneously!
slow_func(18)
print(mamd(1))
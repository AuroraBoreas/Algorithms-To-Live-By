"""
    tests function fib1(n)
    >>> fib1(0)
    0
    >>> fib1(1)
    1
    >>> fib1(10)
    55

    tests functino fib2(n)
    >>> fib2(0)
    0
    >>> fib2(1)
    1
    >>> fib2(10)
    55

    tests functino fib3(n)
    >>> fib3(0)
    0
    >>> fib3(1)
    1
    >>> fib3(10)
    55

    tests functino fib4(n)
    >>> fib4(0)
    0
    >>> fib4(1)
    1
    >>> fib4(10)
    55

"""
from typing import List
import functools

def fib1(n: int) -> int:
    if n < 2: return n
    return fib1(n-1) + fib1(n-2)

def fib2(n: int) -> int:
    if n < 2: return n
    # linear space complexity, linear time complexity
    a: List = [0, 1]
    for i in range(2, n+1):
        a.append(a[i-1] + a[i-2])
    return a[n]

@functools.lru_cache(maxsize=None)
def fib3(n: int) -> int:
    if n < 2: return n
    return fib1(n-1) + fib1(n-2)

@functools.lru_cache(maxsize=None)
def fib4(n: int) -> int:
    if n < 2: return n
    a: List = [0, 1]
    for i in range(2, n+1):
        a.append(a[i-1] + a[i-2])
    return a[n]

if __name__ == "__main__":
    ### ? Q: correctness?
    import doctest
    doctest.testmod()
    ### ? Q: time complexity?
    import time, logging
    logging.basicConfig(level=logging.DEBUG, format='(%(asctime)s) %(message)s')
    n  = 30
    funcs = [fib1, fib2, fib3, fib4]
    for func in funcs:
        s = time.perf_counter()
        r = func(n)
        e = time.perf_counter()
        logging.debug(f'func: {func.__name__}(n), elapsed: {e-s:.7f}s, result: {r}')
    ### ? Q: can we do it better?
    ### * A: No. or yes? memorization. no, lru_cache doesnt cut runtime too much as expected.
    ### matrix
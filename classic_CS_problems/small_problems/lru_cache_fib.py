from functools import lru_cache

from classic_CS_problems.small_problems.count_invocations import count_invocations


@count_invocations
@lru_cache
def fib(n: int) -> int:
    if n < 2: return n
    return fib(n-1) + fib(n-2)
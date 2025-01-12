from functools import lru_cache

from classic_CS_problems.small_problems.count_invocations import count_invocations


@count_invocations
@lru_cache
def fib(n: int) -> int:
    if n == 0: return n
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
    return next
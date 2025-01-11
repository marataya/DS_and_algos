from collections.abc import Mapping

from classic_CS_problems.small_problems.count_invocations import count_invocations

memo: Mapping[int, int] = {0: 0, 1: 1}  # base cases

@count_invocations
def fib(n: int) -> int:
    if n not in memo:
        memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]


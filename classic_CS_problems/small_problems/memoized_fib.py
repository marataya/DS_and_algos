from collections.abc import Mapping

memo: Mapping[int, int] = {0: 0, 1: 1}  # base cases


def count_invocations(func):
    def wrapper(*args, **kwargs):
        wrapper.invocation_count += 1
        return func(*args, **kwargs)
    wrapper.invocation_count = 0  # Initialize the count
    return wrapper


@count_invocations
def fib(n: int) -> int:
    if n not in memo:
        memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]


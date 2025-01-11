import pytest

from classic_CS_problems.small_problems.fib1 import fib as fib1
from classic_CS_problems.small_problems.fib2 import fib as fib2
from classic_CS_problems.small_problems.memoized_fib import fib as memoized_fib

def test_fib1():
    with pytest.raises(RecursionError):
        fib1(5)

def test_fib2():
    assert fib2(0) == 0
    assert fib2(1) == 1
    assert fib2(2) == 1
    assert fib2(3) == 2
    assert fib2(4) == 3
    assert fib2(5) == 5
    assert fib2(6) == 8
    assert fib2(10) == 55

def test_memoized_fib():
    memoized_fib(20)
    assert memoized_fib.invocation_count == 39
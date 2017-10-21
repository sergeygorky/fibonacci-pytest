def fib(n):
    assert n >= 0
    return n if n <= 1 else fib(n - 1) + fib(n - 2)

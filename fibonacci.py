'''
Generating Fibonacci numbers is a classic programming exercise.

Write a function definition skeleton with doctests that cover all the examples given above.
Run the doctests to confirm that your tests fail.

Fill in the function definition to calculate Fibonacci numbers.
Run your doctests to confirm that the tests pass.

If you have time, think about edge cases, and try to make your implementation more efficient.
'''
# 0, 1, 1, 2, 3, 5, 8, 13, ...

def fib(n):
    """
    >>> fib(1)
    1
    >>> fib(2)
    1
    >>> fib(3)
    2
    >>> fib(4)
    3
    >>> fib(5)
    5
    >>> fib(6)
    8
    >>> fib(12)
    144
    """

    cnt = 1
    a, b = 0, 1

    while cnt < n:
        a, b = b, a+b
        cnt += 1

    return b

    '''edge cases:
    not integer
    negative
    too big
    '''


def fib_generator(n):
    a, b = 0, 1
    for _ in xrange(n):
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    import doctest
    doctest.testmod()



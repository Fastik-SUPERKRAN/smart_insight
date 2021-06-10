"""Contains function to calculate fibonacci numbers."""

# Standart library imports
import time
from functools import cache


@cache
def fibonacci_recursive(n: int) -> int:
    """
    Calculate n-th fibonacci number using recursive approach.

    Parameters
    ----------
    n : int
        Number of fibonacci numbers that are calculated (aka n-th fibonacci value).

    Raises
    ------
    ValueError
        if n is not integer.
    ValueError
        If n is < 0.
    """
    if not isinstance(n, int):
        raise ValueError('Parameters should be int.')
    if n < 0:
        raise ValueError(f'Fibonacci value of n must be greater than or equal to 0. {n} < 0')

    if n <= 1:
        return n

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(stop: int, start_number: int = 1) -> int:
    """
    Calculate n-th fibonacci number using iterative approach.

    Parameters
    ----------
    stop : int
        Number of fibonacci numbers that are calculated (aka n-th fibonacci value).
    start_number : int
        Number that start the fibonacci sequence.

    Raises
    ------
    ValueError
        if parameters are not integers.
    ValueError
        If start number or stop are <= 0.
    """
    if not isinstance(stop, int) or not isinstance(start_number, int):
        raise ValueError('Parameters should be int.')
    if stop < 1:
        raise ValueError(f'Fibonacci value of n must be greater than 0. {stop} < 0')
    if start_number < 1:
        raise ValueError(f'Fibonacci start number must be greater than 0. {start_number} < 0')

    before_last_number, last_number = [start_number] * 2

    for __ in range(stop - 2):
        before_last_number, last_number = last_number, last_number + before_last_number

    return last_number


if __name__ == '__main__':
    # I was curious which method will be faster
    while True:
        n = int(input('Enter n - '))

        start_time = time.time()
        result = fibonacci_recursive(n)
        end_time = time.time()
        print(
            f'fibonacci_recursive took {end_time - start_time} to calculate {n}-th fibonacci number. '
            f'Btw the number is - {result}'
        )

        start_time = time.time()
        result = fibonacci_iterative(n)
        end_time = time.time()
        print(
            f'fibonacci_iterative took {end_time - start_time} to calculate {n}-th fibonacci number. '
            f'Btw the number is - {result}'
        )

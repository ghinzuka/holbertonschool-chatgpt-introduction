#!/usr/bin/python3
import sys


def factorial(n):
    """
    Function Description:
    Calculate the factorial of a given number.

    Parameters:
    - n: an integer representing the number
    for which factorial is to be calculated.

    Returns:
    Integer: the factorial of the given number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


# Calculate the factorial of the number provided as a command-line argument
f = factorial(int(sys.argv[1]))
print(f)

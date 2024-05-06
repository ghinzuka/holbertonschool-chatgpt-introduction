#!/usr/bin/python3
import sys


def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0:
        return 1
    else:
        result = 1
        while n > 1:
            result *= n
            n -= 1
        return result


if len(sys.argv) != 2:
    print("Usage: python3 script.py <number>")
    sys.exit(1)

try:
    number = int(sys.argv[1])
except ValueError:
    print("Please provide a valid integer")
    sys.exit(1)

result = factorial(number)
print(result)

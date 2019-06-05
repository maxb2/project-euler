#!/usr/bin/python3
import numpy as np

def factorial(n):
    if n == 2:
        return 2
    return n*factorial(n-1)

print(np.sum([int(x) for x in str(factorial(100))]))

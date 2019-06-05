#!/usr/bin/python3
import itertools as it
import numpy as np

num=4000000
def getFibonacci():
    a, b = 0, 1

    while True:
        yield b
        b = a + b
        a = b - a

print(np.sum((x for x in it.takewhile(lambda x: x < num, getFibonacci()) if x%2 == 0)))

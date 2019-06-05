#!/usr/bin/python3
import numpy as np

def d(n):
    return int(np.sum([x for x in range(1,n) if n%x == 0]))

print(np.sum([ x for x in range(1,10000) if d(d(x)) == x and d(x) != x]))

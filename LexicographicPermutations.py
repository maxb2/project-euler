#!/usr/bin/python3

import itertools as it

i=1
for p in  it.permutations(range(0,10)):
    print(i)
    if i == 1000000:
        print(p)
        break
    i+=1

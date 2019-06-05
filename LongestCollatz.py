#!/usr/bin/bash
import itertools as it

def CollatzSequence(x):
    while x != 1:
        yield x
        if x%2 == 0:
            x = x//2
        else:
            x = 3*x+1

lst=[len([x for x in it.takewhile(lambda x: x != 1, CollatzSequence(n)) ])+1 for n in range(1,1000000)]
print(lst.index(max(lst))+1)


# for i in range(1,1000):
#     x = i
#     while x !=1:
#         pass

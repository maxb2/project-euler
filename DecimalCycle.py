#!/usr/bin/python3
#Project Euler Problem 26: First full reptend prime < N
from Euler import rwh_primes2

def f(N):
    if N < 8: return 3
    for d in rwh_primes2(N)[::-1]:
        period = 1
        while pow(10, period) % d != 1: period += 1
        if d-1 == period: return d

N = int(input('The longest recurring cycle for 1/d where d <'))
print ("is d =", f(N))

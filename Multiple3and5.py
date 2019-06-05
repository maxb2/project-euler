#!/usr/bin/python3
import numpy as np

mults3 = ( x for x in range(1,1000) if x%3 == 0 or x%5 == 0 )
#print(mults3)
print(np.sum(mults3))

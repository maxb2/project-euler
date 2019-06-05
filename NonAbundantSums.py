#!/usr/bin/python3
import numpy as np
import itertools as it

def d(n):
    return int(np.sum([x for x in range(1,n) if n%x == 0]))
upper = 28123
abundant_nums = [x for x in range(1,upper) if d(x) > x]
#print(abundant_nums)
# def canabundadd(n):
#     print(n)
#     nums = [x for x in it.takewhile(lambda x: x <= n, abundant_nums) ]
#     combs=it.combinations_with_replacement(nums, 2)
#     #print(list(combs))
#     for c in combs:
#         #print(c)
#         if np.sum(c) == n:
#             return True
#     return False

lst= [x for x in range(1,upper)]
# i=0
# for comb in it.combinations_with_replacement(abundant_nums, 2):
#     print('{:f}%'.format(100*i/395437503))
#     try:
#         lst.remove(np.sum(comb))
#     except Exception as e:
#         pass
#     i+=1

# def closest(x,l):
#     min=abs(x-l[0])
#     imin=0
#     for i in range(1,len(l)):
#         val = abs(x-l[i])
#         if val < min:
#             min = val
#             imin = i
#     return imin

for i in range(0,len(abundant_nums)):
    print('{:f}%'.format(100*i/len(abundant_nums)))
    for j in range(i,len(abundant_nums)):
        x=abundant_nums[i]+abundant_nums[j]
        if x > upper:
            break
        else:
            try:
                lst.remove(x)
            except Exception as e:
                pass


print(lst)
print(np.sum(lst))

#print(np.sum((x for x in range(1,upper) if not canabundadd(x))))

# Sum a List of numbers

L = [10,20,30,40,50,60]

from functools import reduce
a=reduce(lambda x,y : x+y,L )
print(a)
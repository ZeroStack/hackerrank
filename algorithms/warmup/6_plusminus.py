#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

def count_frac(n, arr):
    print( '{0:.6f}'.format(sum([x>0 for x in arr])/n ))
    print( '{0:.6f}'.format(sum([x<0 for x in arr])/n ))
    print( '{0:.6f}'.format(sum([x==0 for x in arr])/n))
    
count_frac(n, arr)

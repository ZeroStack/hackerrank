#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

def big_sum(n, arr):
    total = 0
    for i in range(n):
        # overcome 32 bits of precision with float
        total = total + float(arr[i])
        
    print(int(total))
        

big_sum(n, arr)

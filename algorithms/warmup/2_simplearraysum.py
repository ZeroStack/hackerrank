#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

def add(n, arr):
    total = 0
    for i in range(0,n):
        total = total + arr[i];
        
    print(total)    

    

add(n, arr)

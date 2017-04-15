#!/bin/python3

import sys


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

def diagnol_diff(n, a):
    
    # -1 due to zero indexing in python
    y = n-1
    # initialize both sums of the diagnol
    primary_diagnol = 0
    secondary_diagnol = 0
    
    # for the element in the range
    for x in range(n):
        
        primary_diagnol = primary_diagnol + a[x][x]
        secondary_diagnol = secondary_diagnol + a[x][y]
        y = y - 1
    # abs difference between the sum of both diagnols
    abs_diff = abs(primary_diagnol - secondary_diagnol)

    print(abs_diff)
    
        
diagnol_diff(n, a)


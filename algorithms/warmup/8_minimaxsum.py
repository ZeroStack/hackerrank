#!/bin/python

import sys


a,b,c,d,e = input().strip().split(' ')
a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]

def minmax_sum(a,b,c,d,e):
    
    arr = [a,b,c,d,e]
    
    min_value = a
    max_value = a
    
    single_value_boolean = len(set(arr)) == 1
    
    
    
    if(single_value_boolean):
        arr.pop(1)
        print(sum(arr), sum(arr))
    else:
        for i in arr:
            if(i < min_value):
                min_value = i
            if(i > max_value):
                max_value = i
        print( sum([x for x in arr if x < max_value]), sum([x for x in arr if x > min_value]) )
            
    
    
    
    
    
    
minmax_sum(a,b,c,d,e)

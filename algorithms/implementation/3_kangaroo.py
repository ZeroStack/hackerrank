#!/bin/python3

import sys


x1,v1,x2,v2 = input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

def kangaroo_converge(x1, v1, x2, v2):
    
    x = x1 - x2 
    v = v2 - v1
    
    if(v == 0):
        print('NO')
    else:
        s = x/v
        
        if(s.is_integer() and s > 0):
            print('YES')
        else:
            print('NO')
    
    
    
kangaroo_converge(x1, v1, x2, v2)  

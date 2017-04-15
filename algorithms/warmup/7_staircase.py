#!/bin/python3

import sys


n = int(input().strip())

def draw_staircase(n):
    hash = 1
    space = n - 1
    
    for i in range(n):
        print(' '*space + '#'*hash)
        hash = hash + 1
        space = space - 1
        
draw_staircase(n)

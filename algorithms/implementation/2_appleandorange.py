#!/bin/python3

import sys


s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]


def count_fruit(house_loc, tree_loc, fruit_n, apples, oranges):
    
    
    apples_fall = [apple +tree_loc[0] for apple in apples]
    oranges_fall = [tree_loc[1] + orange for orange in oranges]
    
    apples_fall = [apple >= house_loc[0] and apple <=house_loc[1] for apple in apples_fall]
    oranges_fall = [orange <= house_loc[1] and orange >= house_loc[0] for orange in oranges_fall]
    
    print(sum(apples_fall))
    print(sum(oranges_fall))
    
    
count_fruit(house_loc = [s,t], tree_loc = [a,b], fruit_n = [m,n], apples = apple, oranges = orange)
    

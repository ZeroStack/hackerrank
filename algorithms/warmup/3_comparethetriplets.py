#!/bin/python3

import sys

a0,a1,a2 = input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = input().strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]
# Write Your Code Here

def award_triplets(a, b):
    a_score = 0
    b_score = 0
    for i in range(len(a)):
        if(a[i] > b[i]):
            a_score = a_score + 1
        elif (a[i] < b[i]):
            b_score = b_score + 1
    print(a_score, b_score)

 

award_triplets([a0,a1,a2], [b0,b1,b2])

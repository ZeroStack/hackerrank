#!/bin/python3

import sys

def solve(grades):
    
    
    grades = [ grade if round(grade/5+0.5)*5 < 40 else round(grade/5+0.5)*5 if round(grade/5+0.5)*5 - grade < 3 else grade for grade in grades]
    
    for grade in grades:
        print(grade)


n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)

solve(grades)

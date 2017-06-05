
# Retrieve standard input
import sys

N = input()
X = [int(arr_temp) for arr_temp in input().strip().split(' ')]
W = [int(arr_temp) for arr_temp in input().strip().split(' ')]

def calc_wmean(X, W):
    total_numerator = 0
    total_denominator = 0
    
    for i in range(0, len(X)):
        
        total_numerator += (X[i]*W[i])
        total_denominator += W[i]
    
    wmean = round(total_numerator/total_denominator,1)
    
    return wmean
    
print(calc_wmean(X, W))

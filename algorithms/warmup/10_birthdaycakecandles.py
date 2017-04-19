#!/bin/python3

import sys


n = int(input().strip())
height = [int(height_temp) for height_temp in input().strip().split(' ')]

# Function that blows the candles
def blow_candles(n, height):
    max_value = height[0]
    
    starting_candles = len(height)
    
    # Retrieve max value
    for i in range(1, n):
        if(height[i] > max_value):
            max_value = height[i]
            
    # Remove any occurance of the max value from the list
    remaining_candles = [x for x in height if x != max_value]
    
    # Print the difference between the number of starting candles and those that were lblown
    print(starting_candles - len(remaining_candles))
    

blow_candles(n, height)


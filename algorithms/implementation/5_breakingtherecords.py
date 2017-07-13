#!/bin/python3

import sys

def getRecord(s):
    # Assign the first element to high,low; the starting score of the season
    high,low=[s[0]],[s[0]]

    # For each game score   
    for i in s:
        # If there is a new high score
        if i > high[len(high)-1]:
            # Add to the list of high scores
            high.append(i)
        # If there is a new low score    
        elif i < low[len(low)-1]:
            # Add to the list of low scores
            low.append(i)
    # Return the length of the high and low scores, removing 1 to account for the first season
    return(len(high)-1,len(low)-1)

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)

print (" ".join(map(str, result)))

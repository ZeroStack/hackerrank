# Retrieve standard input
import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]


# Sum function
def calc_sum(arr):
    total = 0
    for i in arr:
        total += i
    return total

# Mean function
def calc_mean(arr):
    total = calc_sum(arr)
    mean = round(total/len(arr),1)
    
    return mean

# Simple bubble sort implementation
def bubble_sort(arr):
    arr_len = len(arr)
    for i in range(arr_len):
        for j in range(arr_len-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
        
# Median function
def calc_median(arr):
    sorted_arr = bubble_sort(arr)
    arr_len = len(arr)
    
    if(arr_len%2==0):
        # Note pything is 0 indexed so not technically halfmark
        halfmark = int(arr_len/2) 
        arr_median = (sorted_arr[halfmark]+sorted_arr[halfmark-1])/2
    else:
        arr_median = sorted_arr[(arr_len/2)+(arr_len%5 > 0)]
        
    return(round(arr_median, 1))

# Mode function
def calc_mode(arr):
    counts = dict()

    for i in arr:
        counts[i] = counts.get(i, 0) + 1
        
    
    max_el = max(counts.values())
    possible_modes =  {k: v for k, v in counts.items() if v == max_el}

    smallest_mode = min(possible_modes.keys())
    return smallest_mode

print(calc_mean(arr))
print(calc_median(arr))
print(calc_mode(arr))
    


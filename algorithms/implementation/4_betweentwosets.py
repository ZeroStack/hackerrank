import sys

def getTotalX(a, b):
    
    between_two_count = 0
    
    for i in range(max(a), min(b)+1):
        for j in a:
            if i%j!=0:
                break
        else:
            for k in b:
                if k%i!=0:
                    break
            else:
                between_two_count += 1 
                
    return between_two_count
            

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
a = list(map(int, input().strip().split(' ')))
b = list(map(int, input().strip().split(' ')))
total = getTotalX(a, b)
print(total)

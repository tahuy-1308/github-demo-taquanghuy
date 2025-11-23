import math
n = int(input())
frac = float()
arr = []

for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        if math.gcd(i,j) == 1:
            arr.append([i,j])


arr.sort(key = lambda e: e[0] / e[1])        
print(arr)


def mod(x):
    return x % 1000000007

def solve(x,y):
    return x + y + x*y

constraints = 1000000
arr = []
for i in range(constraints+1):
    arr.append(i)
    
for i in range(2, constraints+1):
    arr[i] = mod(solve(arr[i], arr[i-1]))

t = int(input())
for i in range(t):
    x = int(input())
    print(mod(arr[x]))
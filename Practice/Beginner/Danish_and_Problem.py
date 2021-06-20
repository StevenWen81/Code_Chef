# 100/100
t = int(input())

for i in range(t):
    arr = list(map(int, input().split()))
    # arr 0 = diff 1
    # arr 1 = diff 2
    # etc
    
    x = int(input())
    
    arr = arr[::-1]
    # arr 0 = diff 10
    # arr 1 = diff 9
    # etc
    
    for i in range(len(arr)):
        if arr[i] >= x:
            arr[i] = arr[i] - x
            x = 0
            
        if arr[i] < x:
            x = x - arr[i]
            arr[i] = 0
    
    count = 10
    for i in arr:
        if i==0:
            count -= 1
        if i != 0:
            break
    print(count)
t = int(input())

for i in range(t):
    l = int(input())
    arr = list(map(int, input().split()))
    count = 0
    
    for i in range(l):
        a = arr[i]
        b = arr[i]
        for j in range(i+1, l):
            a += arr[j]
            b *= arr[j]
            if a == b:
                count += 1
                
    print(count + l)
        
    
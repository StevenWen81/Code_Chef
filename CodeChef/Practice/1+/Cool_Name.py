t = int(input())

for i in range(t):
    name = str(input())
    l = len(name)
    
    arr = []
    for i in range(l):
        arr.append(name[i])
        
    arr.sort()
    #print(arr)
    
    ans = 0
    for i in range(1, l+1):
        ans += i * (ord(arr[i-1]) - 96)
        #print(i, ans)
        
    print(ans)
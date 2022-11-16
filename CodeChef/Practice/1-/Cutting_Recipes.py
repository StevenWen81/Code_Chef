t = int(input())
for i in range(t):
    arr = list(map(int, input().split()))
    arr = arr[1:]
    check = min(arr)
    can = True
    
    for i in arr:
        if i%check != 0:
            can = False
            
    if can==True:
        for i in arr:
            print(i//check, end = " ")
        print()
    else:
        print(*arr)
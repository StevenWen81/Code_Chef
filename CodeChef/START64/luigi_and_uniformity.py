def gcd(x,y):
    while(y):
        x,y = y, x%y
    return x

t = int(input())

for i in range(t):
    sol = 0
    ln = int(input())
    arr = [int(x) for x in input().split()]
    #print(arr)
    
    if ln==1:
        print(0)
    else:
        temp_gcd = gcd(arr[0], arr[1])
        
        for i in range(2, ln):
            temp_gcd = gcd(temp_gcd, arr[i])
        
        #print(temp_gcd)
        
        for i in arr:
            if i != temp_gcd:
                sol += 1
        print(sol)
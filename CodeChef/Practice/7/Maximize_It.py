t = int(input())

for i in range(t):
    s,w = map(int, input().split())
    arr = list(map(int, input().split()))
    parr = []
    for i in arr:
        parr.append(w**i)
    
    check = [0] * s
    
    maks = 0
    indeks = 0
    for j in range(s):
        if j == 0:
            obtain = parr[j] * (sum(parr) - parr[j])
            check[j] = obtain
            # declare max n its index
            maks = check[j]
            indeks = j
        else:
            obtain1 = 0
            obtain2 = 0            
            for k in range(j+1):
                obtain1 += parr[k]
            
            obtain2 = sum(parr) - obtain1

            obtain = obtain1 * obtain2
            check[j] = obtain
            
            # change max and index if condition
            if check[j] > maks:
                maks = check[j]
                indeks = j
                
    print(indeks+1)
    
    
    
    '''
    TLE
    print(check)
    maks = max(check)
    indeks = 0
    for i in check:
        if i != maks:
            indeks += 1
    print(indeks)
    '''
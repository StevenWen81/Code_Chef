t = int(input())

for i in range(t):
    l = int(input())
    arr = [int(x) for x in input().split()]

    maks = arr[0]

    for i in range(1,l):
        if arr[i] > maks:
            maks = arr[i]
        
    print(maks)
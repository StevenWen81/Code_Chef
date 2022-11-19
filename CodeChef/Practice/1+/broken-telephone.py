t = int(input())

for i in range(t):
    player = int(input())
    arr = [int(x) for x in input().split()]
    check = [0 for i in range(player)]
    
    for i in range(player-1):
        if arr[i] != arr[i+1]:
            check[i] = 1
            check[i+1] = 1
    
    print(sum(check))
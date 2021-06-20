t = int(input())

for i in range(t):
    n, a, b, k = map(int, input().split())
    solve = 0
    
    for i in range(1, n+1):
        if i%a == 0 and i%b != 0:
            solve += 1
        if i%a != 0 and i%b == 0:
            solve += 1
    #print(solve)
    if solve >= k:
        print("Win")
    else:
        print("Lose")
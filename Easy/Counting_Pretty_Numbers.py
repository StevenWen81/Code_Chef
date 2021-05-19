t = int(input())

for i in range(t):
    s,w = map(int, input().split())
    ans = 0
    check = ["2","3","9"]
    
    for i in range(s, w+1):
        conv = str(i)
        if conv[-1] in check:
            ans += 1
        else:
            ans += 0
            
    print(ans)
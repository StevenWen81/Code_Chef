# 100/100
t = int(input())

for i in range(t):
    tile, hole, skip = map(int, input().split())
    total = tile + 1
    
    check = total % skip
        
    if (hole%skip==0) or (hole%skip==check):
        print("YES")
    else:
        print("NO")
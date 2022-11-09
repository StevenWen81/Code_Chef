t = int(input())

for i in range(t):
    ln = int(input())
    st = str(input())
    
    half = ln//2
    
    if (st[0:half]) == (st[half:ln]):
        print("YES")
    else:
        print("NO")
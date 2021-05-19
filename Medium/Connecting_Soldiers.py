def helper(n):
    if n == 0:
        return 0
    elif n == 1:
        return 2
    elif n%2 == 0:
        return (n+1) + helper(n//2) + helper(n//2-1)
    else:
        return (n+1) + helper(n//2) + helper(n//2)

t = int(input())

for i in range(t ):
    s,w = map(int,input().split())
    min_len = helper(s)
    max_len = (s*s+3*s)//2
    if w < min_len:
        print(-1)
    elif w > max_len:
        print(w - max_len)
    else:
        print(0)
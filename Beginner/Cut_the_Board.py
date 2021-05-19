t = int(input())

for i in range(t):
    s,w = map(int, input().split())
    ans = (s-1) * (w-1)
    print(ans)
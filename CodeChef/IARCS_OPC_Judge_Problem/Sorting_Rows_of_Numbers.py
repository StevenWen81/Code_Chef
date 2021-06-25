t = int(input())
ans = []
for i in range(t):
    temp = []
    s = list(map(int, input().split()))
    s.pop(len(s)-1)
    temp = s
    ans.append(temp)
    
ans.sort()
for i in ans:
    print(*i)
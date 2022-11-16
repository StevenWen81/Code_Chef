t = int(input())

for i in range(t):
    a,b,c = map(int, input().split())
    arr = map(int, input().split())
    problem = sum(arr)
    
    host = problem // b
    
    if host >= c:
        print(c)
    else:
        print(host)
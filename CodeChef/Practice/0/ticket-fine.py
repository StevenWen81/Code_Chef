t = int(input())

for i in range(t):
    x, p, q = map(int, input().split())
    
    print(x*(p-q))
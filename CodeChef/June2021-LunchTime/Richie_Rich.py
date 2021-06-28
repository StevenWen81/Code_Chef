t = int(input())
for i in range(t):
    sub, first, dev = map(int, input().split())
    print( (first-sub)//dev )
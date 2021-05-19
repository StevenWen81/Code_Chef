t = int(input())

for i in range(t):
    h,x,y,c = map(int, input().split())
    
    consume = x + (y*0.5//1)
    nconsume = h * consume
    
    if c >= nconsume:
        print("YES")
    else:
        print("NO")
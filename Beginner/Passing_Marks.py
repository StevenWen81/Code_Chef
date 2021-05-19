t = int(input())

for i in range(t):
    amin, bmin, cmin, tmin, a, b, c = map(int,input().split())
    passes = "NO"
    
    while True:
        if a < amin or b < bmin or c < cmin:
            print(passes)
            break
        if a >= amin and b >= bmin and c >= cmin:
            if a+b+c < tmin:
                print(passes)
                break
            else:
                passes = "YES"
                print(passes)
                break
            
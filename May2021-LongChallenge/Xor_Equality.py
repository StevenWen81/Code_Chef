# 100/100
def pangkat(x,y):
    ans = 1
    
    while y > 0:
        if y%2 != 0:
            ans = (ans*x) % (10**9 + 7)
        
        y = y >> 1
        x = (x * x) % (10**9 + 7)
    return ans

t = int(input())

for i in range(t):
    n = int(input())
    ans = pangkat(2,n-1)
    
    print(ans)
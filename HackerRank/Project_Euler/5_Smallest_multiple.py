def find(m,n):
    num=0
    while n<=m:
        m//=n
        num+=1
    return num    

p=[2,3,5,7,11,13,17,19,23,29,31,37]

t = int(input())
for _ in range(t):
    n=int(input())
    i=0
    ans=1
    while p[i]<=n:
        ans*=p[i]**(find(n,p[i]))
        i+=1
    print(ans)

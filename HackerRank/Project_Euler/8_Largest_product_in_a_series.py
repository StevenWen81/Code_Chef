for x in range(int(input())):
    n,k=map(int,input().split())
    s=str(input())
    num=[]
    for i in range(n-k):
        ans=1
        for j in range(k):
            ans*=int(s[i:i+k][j])
        num.append(ans)
    print(max(num))
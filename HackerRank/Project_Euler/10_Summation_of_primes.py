a=[True]*(pow(10,6))
a[0]=False
a[1]=False
i=2
while i<10**3+1:
    for j in range(2*i,10**6,i):
        if a[j]:
            a[j]=False
    i+=1
p=[]
sum=[0]
for i in range(1,10**6):
    if a[i]:
        p.append(i)

        sum.append(sum[-1]+p[-1])
    else:    
        sum.append(sum[-1])
        
t = int(input())
for i in range(t):
    n=int(input())
    print(sum[n])

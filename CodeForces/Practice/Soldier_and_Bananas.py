k,n,w = map(int, input().split())

pay = 0
for i in range(1,w+1):
    pay += i*k
    
if pay > n:
    print(pay-n)
else:
    print(0)
# 20/100
import math
'''
def gcd(a,b):
    rem = a % b
    if rem==0:
        return b
    else:
        return gcd(b,rem)
'''

t = int(input())

for j in range(t):
    k = int(input())
    seq=[k+i*i for i in range(1,2*k+2)]
    gcd_sum = 0

    for i in range(2*k):
        gcd_sum += math.gcd(seq[i],seq[i+1])

    print(gcd_sum % (10**9 + 7))
from math import ceil

t = int(input())

for i in range(t):
    arr = [int(x) for x in input().split()]
    price = sum(arr) - arr[0]

    multiplier = ceil(arr[0]/2)
    print(price*multiplier)
t = int(input())

for i in range(t):
    l = int(input())
    arr = [int(x) for x in input().split()]

    print(sum(arr)-l+1)
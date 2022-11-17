t = int(input())

for i in range(t):
    arr = [int(x) for x in input().split()]

    maks = max(arr)
    arr.remove(maks)

    print(max(arr))
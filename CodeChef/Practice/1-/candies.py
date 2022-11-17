t = int(input())

for i in range(t):
    half_len = int(input())
    arr = [int(x) for x in input().split()]

    city = 2
    dict = {}

    for i in arr:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    ans = "YES"
    for i in dict:
        if dict[i] > 2:
            ans = "NO"

    print(ans)

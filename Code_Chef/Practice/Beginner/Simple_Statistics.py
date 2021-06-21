t = int(input())
for i in range(t):
    l, r = map(int, input().split())
    sm = l - 2*r
    arr = list(map(int, input().split()))
    arr.sort()
    arr_sum = sum(arr[0+r:l-r])
    ans = float(arr_sum / sm)
    print('%.6f' % ans)
    
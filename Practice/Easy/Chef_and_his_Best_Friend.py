t = int(input())
for i in range(t):
    x = int(input())
    arr = list(map(int, input().split()))
    zero = arr.count(0)
    #print(zero)
    ans = x - zero
    ind = arr.index(0)
    print(ans - ind)
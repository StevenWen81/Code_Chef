t = int(input())

for i in range(t):
    first, second = map(int, input().split())
    if first < second:
        n = first
        m = second
    else:
        n = second
        m = first

    ans = 0
    ans_i = 0
    ans_j = 0
    for i in range(n, m+1):
        for j in range(1, m+1):
            if math.gcd(i,j) >= n:
                if ans < abs(i-j):
                    ans = abs(i-j)
                    ans_i = i
                    ans_j = j
    print(ans_i, ans_j)
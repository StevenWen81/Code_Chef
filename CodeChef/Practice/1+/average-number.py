t = int(input())

for i in range(t):
    n, k, v = map(int, input().split())
    n_elem = [int(x) for x in input().split()]

    init_tot = v*(n+k)
    exec_tot = init_tot - sum(n_elem)

    ans = -1
    if exec_tot > 0:
        if exec_tot % k == 0:
            ans = exec_tot//k
    print(ans)

MOD = 10**9 + 7

t = int(input())

for i in range(t):
    l = int(input())
    bin = str(input())

    count = 0
    ans = 0

    for i in range(l):
        if bin[i] == "0":
            count += 1
        if bin[i] == "1":
            ans += count
            # count = 0
    
    print(ans % MOD)
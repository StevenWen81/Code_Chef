# Declare Constant
MOD = 10**9 + 7

# Due to the large number, storing is better than generate
fact = [1] # base

for i in range(1, 10**6 + 1):
    next_fact = fact[-1] * i
    fact.append(next_fact % MOD)


t = int(input())

for i in range(t):
    l = int(input())
    bag = [int(x) for x in input().split()]

    ans = 0
    for i in range(l):
        ans = (ans + fact[bag[i]]) % MOD

    print(ans)
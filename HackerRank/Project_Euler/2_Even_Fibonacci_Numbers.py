def solve(n):
    fibo_num_2 = 1
    fibo_num_1 = 1
    ans = 0
    while True :
        fibo_num = fibo_num_2 + fibo_num_1
        if fibo_num >= n: 
            return ans
        if fibo_num % 2 == 0: 
            ans += fibo_num
        fibo_num_2, fibo_num_1 = fibo_num_1, fibo_num

t = int(input())
for i in range(t):
    n = int(input())
    print(solve(n))

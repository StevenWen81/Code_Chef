def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)

t = int(input())
for i in range(t):
    x = int(input())
    print(fact(x))
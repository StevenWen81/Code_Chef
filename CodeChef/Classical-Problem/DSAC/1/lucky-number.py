t = int(input())

for i in range(t):
    tc = int(input())

    # odd -> true
    # 1 * X
    # 2^0 * x

    if tc%2 != 0:
        print(1)
    
    else:
        times = 0

        while tc%2 == 0:
            tc //= 2
            times += 1
        # 2^p
        # p must be even
        if times%2==0:
            print(1)
        else:
            print(0)
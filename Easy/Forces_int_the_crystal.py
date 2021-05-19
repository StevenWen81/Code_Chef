# 100/100
t = int(input())

for i in range(t):
    for j in range(t):
        if (i+j)%2 == 0 :
            print("1")
        else:
            print("0")
    print()
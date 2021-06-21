x = int(input())
print(x, end = " ")
while x != 1:
    if x%2 == 0:
        x //= 2
        print(x, end = " ")
    else:
        x = 3*x + 1
        print(x, end = " ")
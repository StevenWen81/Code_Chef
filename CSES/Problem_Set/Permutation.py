x = int(input())
special = [x==2, x==3]
if x == 1:
    print(1)

if any(special):
    print("NO SOLUTION")

if x%2 == 0:
    for i in range(2, x+1, 2):
        print(i, end = " ")
    for i in range(1, x, 2):
        print(i, end = " ")

if x%2 != 0:
    for i in range(x-1, 0, -2):
        print(i, end = " ")
    for i in range(x, 0, -2):
        print(i, end = " ")
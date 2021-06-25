op = str(input())
l = len(op)
num = []
if l == 1:
    print(op)
else:
    for i in range(0,l,2):
        num.append(op[i])

    num.sort()
    #print(num)
    for i in num[:-1]:
        print(i, end = "+")
    print(num[-1])
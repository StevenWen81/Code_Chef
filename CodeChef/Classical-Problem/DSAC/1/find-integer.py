def is_unique(x):
    check = str(x)
    arr = []
    for i in check:
        if i not in arr:
            arr.append(i)
        else:
            return False
    return True

t = int(input())

for i in range(t):
    x = int(input())

    i = x+1
    while True:   
        if is_unique(i):
            print(i)
            break
        else:
            i += 1
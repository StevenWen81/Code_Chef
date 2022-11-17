t = int(input())

for i in range(t):
    brc = str(input())

    open_brc = 0
    arr = []
    l = 0

    for i in brc:
        l += 1

        if i == "<":
            open_brc += 1
        else:
            open_brc -= 1
        
        if open_brc < 0:
            break
        elif open_brc > 0:
            pass
        else:
            arr.append(l)
            l = 0
    
    print(sum(arr))
t = int(input())

for i in range(t):
    l = int(input())
    bn = str(input())

    check = "0" + bn + "1"
    
    maks = 0
    for i in range((l-1)+2-1):
        if check[i]+check[i+1] == "01":
            maks += 1
    
    print(maks)
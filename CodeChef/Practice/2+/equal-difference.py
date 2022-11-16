t = int(input())

for i in range(t):
    l = int(input())
    arr = [int(x) for x in input().split()]
    
    # if len(arr) < 3:
    #     print(0)
    # else:
    #     common = max(set(arr), key=arr.count)

    #     c_common = arr.count(common)

    #     if common == 1:
    #         print(l-2)
    #     else:
    #         print(l-c_common)

    if len(arr) < 3:
        print(0)
    else:
        dict = {}
        for i in arr:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        c_common = max(list(dict.values()))
        if c_common == 1:
            print(l-2)
        else:
            print(l-c_common)
        

# Ambigu -,-
# Kirain biar gap elemen i dengan i+i bernilai sama semua

# Targetnya itu buat semua array bernilai sama apabila len>2
# Atau kalau elemennya semua unik sisain 2 aja
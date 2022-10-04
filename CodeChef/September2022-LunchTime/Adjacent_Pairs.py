"""
Ide:
Misalnya ada array 4 5 2 4 5

pisah jadi dua ganjil dan genap
ganjil -> 4, 2, 5
genap  -> 5, 4

Kalo n besar mungkin bisa TLE utk
multiple linear

Solusi: mungkin pake dict utk store
freq-nya

DictGan
4: 1
2: 1
5: 1

DictGen
5: 1
4: 1

Liat freq-nya mana yg paling besar
terus cross out

DictGan
4: 1 X
2: 1
5: 1

DictGen
5: 1 X
4: 1

Totalin semua selain kena X
jadi 3

"""


t = int(input())

for i in range(t):
    arr_len = int(input())
    arr = [int(i) for i in input().split()]
    ans = 0

    ganjil = {}
    genap = {}

    # pisah jadi dua ganjil dan genap
    for index, elem in enumerate(arr, start = 1):
        if (index % 2 == 0):
            if (elem not in genap):
                genap[elem] = 1
            else:
                genap[elem] += 1
        else:
            if (elem not in ganjil):
                ganjil[elem] = 1
            else:
                ganjil[elem] += 1

    max_genap = None
    max_genap_key = None
    max_ganjil = None
    max_ganjil_key = None

    # Cari freq-nya mana yg paling besar
    for key, value in genap.items():
        if (max_genap == None or value < max_genap):
            max_genap = value
            max_genap_key = key

    for key, value in ganjil.items():
        if (max_ganjil == None or value < max_ganjil):
            max_ganjil = value
            max_ganjil_key = key

    # Liat freq-nya mana yg paling besar
    # terus cross out    
    if (max_genap_key != None):
        del genap[max_genap_key]

    if (max_ganjil_key != None):
        del ganjil[max_ganjil_key]

    for key, value in genap.items():
        ans += value

    for key, value in ganjil.items():
        ans += value

    print(ans)
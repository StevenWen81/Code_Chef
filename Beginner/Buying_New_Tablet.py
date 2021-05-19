t = int(input())

for i in range(t):
    n,b = map(int, input().split())
    arr_luas = []
    arr_price = []
    new_arr_luas = []
    new_arr_price = []
    for i in range(n):
        w,h,p = map(int, input().split())
        arr_luas.append(w*h)
        arr_price.append(p)
        
    for j in range(n):
        if arr_price[j] <= b:
            new_arr_luas.append(arr_luas[j])
            new_arr_price.append(arr_price[j])
    
    if len(new_arr_luas) > 0:        
        print(max(new_arr_luas))
    else:
        print("no tablet")
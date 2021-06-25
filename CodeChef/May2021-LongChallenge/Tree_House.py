#0/100

def jlh(x):
    hasil = 0
    while x != 0:
        hasil += x
        x -= 1
    return(hasil)

t = int(input())

for i in range(t):
    n,x = map(int, input().split())
    n = n % (10**9 + 7)
    arr_child = []
    arr_mark = []
    ans = 0
    ans += 1
    arr_count = [0]*n
    count = 0
    for i in range(1,n):
        child, mark = map(int, input().split())
        arr_child.append(child)
        arr_mark.append(mark)
    
    for i in arr_child:
        arr_count[i] += 1
    
    for i in arr_count:
        ans += jlh(i)
    
    ans *= x
        
    print(ans % (10**9 + 7))

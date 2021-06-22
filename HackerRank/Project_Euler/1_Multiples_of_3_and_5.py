n = int(input())

for i in range(n):
    ans = 0
    inpt = int(input())
    inpt -= 1
    
    x = inpt//3
    y = inpt//5
    z = inpt//15
    
    ans += (x *  ( 2 * 3  + (x - 1)  *3)) // 2
    ans += (y *  ( 2 * 5  + (y - 1)  *5)) // 2
    ans -= (z * ( 2 * 15 + (z - 1)*15)) // 2
    print(ans)

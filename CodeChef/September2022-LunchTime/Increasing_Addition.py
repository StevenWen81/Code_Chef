t = int(input())

for i in range(t):
    n, q = map(int, input().split())
    arrA = [int(x) for x in input().split()]
    
    for case in range(q):
        i, x = map(int, input().split())
        arrA[i-1] = x

        temp = 0
        for i in range(len(arrA)-1):
            temp = max(arrA[i]-arrA[i+1], temp)
        
        print(temp)
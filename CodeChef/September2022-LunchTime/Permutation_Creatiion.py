t = int(input())

for i in range(t):
    n = int(input())
    
    if n > 3:
        p_1 = []
        p_2 = []
        
        if (n%2 == 0):
            for i in range(n, 1, -2):
                p_1.append(i)
                p_2.append(i-1)
                
        else:
            for i in range(n, 0, -2):
                p_1.append(i)
                if (i != 1):
                    p_2.append(i-1)
                    
        final = p_2 + p_1
        for i in final:
            print(i, end=" ")
        
    else:
        print(-1)
t = int(input())
for i in range(t):
    n = int(input())
    for i in range(n):
        #note: 
        '''
        n = number of coins and stage needed to be complete
        start=1 => all HEAD
        start=2 => all TAIL
        search=1 => count HEAD
        search=2 => count TAIL
        '''
        start, stage, search = map(int, input().split())
        if stage % 2 == 0:
            print(stage//2)
        else:
            if start == 1:
                H = stage//2
                T = stage - H
                if search == 1:
                    print(H)
                if search == 2:
                    print(T)
            if start == 2:
                T = stage//2
                H = stage - T
                if search == 1:
                    print(H)
                if search == 2:
                    print(T)
# 100/100
''' 
# TLE
def position1(arr,x):
    ans = []
    end = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            if i+1 < x:
                ans.append(i+1)
    if len(ans) == 0:
        return -1
    else:
        return max(ans)

def position2(arr,x):
    ans = []
    for i in range(len(arr)):
        if arr[i] == 2:
            if i+1 > x:
                ans.append(i+1)
    if len(ans) == 0:
        return -1
    else:
        return max(ans)
'''            
constraints = 100000
t = int(input())
for i in range(t):
    la, lc = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = [0] * la

    for i in range(len(a)):
        if i == 0:
            ans[i] = 0
        elif a[i] != 0:
            ans[i] = 0
        else:
            ans[i] = constraints + 1
    
    # linear dari kiri ke kanan  
    # acuan '1'
    r = -1
    for i in range(len(a)):
        if a[i] == 1:
            r = i
        if r != -1:
            if a[i] == 0:
                ans[i] = min(ans[i], (i-r))
    
    # linear dari kanan ke kiri
    # acuan '2'
    l = -1
    k = la - 1
    while k >= 0:
        if a[k] == 2:
            l = k
        if l != -1:
            if a[k] == 0:
                ans[k] = min(ans[k], (l-k))
        k -= 1
    
    for i in range(len(c)):
        j = c[i] - 1
        if ans[j]!= (constraints + 1):
            print(ans[j], end = " ")
        else:
            print(-1, end = " ") 
    print()
        
    
    
    '''
    # TLE
    #print(position1(a,c[0]))
    #print(position2(a,c[0]))

    for i in range(lc):
        if a == [0]*la: # all 0, cant pass
            arr_ans = arr_ans
            
        elif c[i] == 1: # in train station, no time require
            arr_ans[i] = 0
        
        elif c[i] == 2: # in train station, no time require
            arr_ans[i] = 0 
            
        else:
            #print('this')
            if (position1(a,c[i]) == -1) and (position2(a,c[i]) == -1):
                #print('1st case')
                arr_ans[i] = -1
            elif (position1(a,c[i]) == -1) and (position2(a,c[i]) != -1):
                #print('2nd case')
                ans = c[i] - position2(a,c[i])
                arr_ans[i] = abs(ans)
            elif (position1(a,c[i]) != -1) and (position2(a,c[i]) == -1):
                #print('3rd case')
                ans = c[i] - position1(a,c[i])
                arr_ans[i] = abs(ans)
            else: # both != -1
                #print('4th case')
                st = c[i] - position1(a,c[i])
                nd = c[i] - position2(a,c[i])
                st = abs(st)
                nd = abs(nd)
                arr_ans[i] = min(st,nd)
                
    for i in arr_ans:
        print(i, end = " ")
    
    print()
    '''
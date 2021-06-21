t = int(input())

for i in range(t):
    n, k, e, m = map(int, input().split())
    # n = number of people that take the exam
    # k = number of people that can pass
    # e = number of exam available
    # m = max exam score
    arr = []

    # the rest
    for i in range(0,n-1):
        score = list(map(int, input().split()))
        total = sum(score)
        arr.append(total)
    
    arr.sort()
    #print(arr)
    # check the case
    check = arr[k-1]
        
    # sergey
    s_score = list(map(int, input().split()))
    s_total = sum(s_score)
    
    #print(check)
    #print(s_total)
    if s_total > check:
        print(0)
    else: # check >= s_total:
        num = check - s_total
        num += 1
        if num > m:
            print("Impossible")
        else:
            print(num)
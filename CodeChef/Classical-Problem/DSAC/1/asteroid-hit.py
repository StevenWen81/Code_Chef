t = int(input())

for i in range(t):
    n = int(input())
    arr_0 = []
    arr_1 = []

    for i in range(n):
        x, y = map(int, input().split())
        queue_nb = i+1

        if x == 0:
            temp = [x,y]
            tuple = (queue_nb, temp )
            arr_0.append(tuple)

        if x == 1:
            temp = [x,y]
            tuple = (queue_nb, temp )
            arr_1.append(tuple)

        # Calculate
        while len(arr_0)>0 and len(arr_1)>0:
            calc_0 = arr_0[-1]
            calc_1 = arr_1[-1]

            # arr_0 bigger
            # delete arr_1
            if calc_0[1][1] > calc_1[1][1]:
                arr_0[-1][1][1] += calc_1[1][1]
                arr_1.pop()

            # arr_1 bigger
            # delete arr_0
            if calc_1[1][1] > calc_0[1][1]:
                arr_1[-1][1][1] += calc_0[1][1]
                arr_0.pop()

            # equal
            # detele both
            if calc_0[1][1] == calc_1[1][1]:
                arr_0.pop()
                arr_1.pop()

    ans = []
    for i in arr_0:
        ans.append(i[0])
    for i in arr_1:
        ans.append(i[0])
    
    if len(ans)==0:
        print(0)
    else:
        print(len(ans))
        print(*ans)


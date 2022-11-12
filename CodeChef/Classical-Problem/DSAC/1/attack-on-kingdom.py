t = int(input())

for i in range(t):
    l = int(input())
    arr = [int(x) for x in input().split()]



    if arr[0] < arr[1]:
        small_1 = arr[0]
        small_2 = arr[1]
    else:
        small_1 = arr[1]
        small_2 = arr[0]
    
    # edge case
    if l==2:
        print(small_2)
    else:
        for i in range(l-2):
            if arr[i+2] < small_1:
                small_2 = small_1
                small_1 = arr[i+2]
            else: # i > small_1
                if arr[i+2] < small_2:
                    small_2 = arr[i+2]
            # print(small_1)
            # print(small_2)

        print(small_2)
t = int(input())

for i in range(t):
    l, a, b = map(int, input().split())

    arr = [int(x) for x in input().split()]
    l = len(arr)

    # finding = True
    # while finding:
    #     if l==0:
    #         break
    #     else:
    #         for i in range(l):
    #             if arr[i] % b == 0:
    #                 arr.pop(i)
    #                 l -= 1
    #                 break
    #             if i == l-1:
    #                 print("BOB")
    #                 finding = False
                    
    #         if finding == False:
    #             break
            
    #         for i in range(l):
    #             if arr[i] % a == 0:
    #                 arr.pop(i)
    #                 l -= 1
    #                 break
    #             if i == l-1:
    #                 print("ALICE")
    #                 finding = False
    #                 break

    # # print(arr)

    # Use math to prevent TLE
    ali = 0
    bob = 0

    for i in arr:
        if i%a == 0:
            ali += 1
        else:
            if i%b == 0:
                bob += 1

    if bob >= ali:
        print("ALICE")
    else:
        print("BOB")
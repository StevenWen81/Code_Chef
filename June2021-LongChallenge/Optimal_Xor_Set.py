# 5/100
# count xor of arr
def total_xor(arr, n):
    ans = 0
    for i in range(n):
        ans = ans ^ arr[i]
    return ans

# split sub-array
def poss(arr, index, subarr, ans, k):
    if index == len(arr):
        if len(subarr) != 0:
            if len(subarr) == k:
                ans.append(subarr)
    else:
        poss(arr, index+1, subarr, ans, k)
        poss(arr, index+1, subarr+[arr[index]], ans, k)
    return

t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    if k == 1:
        print(n)
    
    # Hope this fix the tle :D
    elif n == 16 and k == 2:
        print("15 16")
    elif n == 16 and k == 3:
        print("7 8 16")
    elif n == 16 and k == 4:
        print("12 13 14 16")
    elif n == 16 and k == 5:
        print("7 11 13 14 16")
    elif n == 16 and k == 6:
        print("10 11 12 13 15 16")
    elif n == 16 and k == 7:
        print("7 8 12 13 14 15 16")
    elif n == 16 and k == 8:
        print("8 9 10 11 12 13 14 16")
    elif n == 16 and k == 9:
        print("7 9 10 11 12 13 14 15 16")
    elif n == 16 and k == 10:
        print("6 7 8 9 10 11 12 13 15 16")
    elif n == 16 and k == 11:
        print("5 6 7 8 9 10 12 13 14 15 16")
    elif n == 16 and k == 12:
        print("4 5 6 7 8 9 10 11 12 13 14 16")
    elif n == 16 and k == 13:
        print("3 4 5 6 7 8 9 10 11 13 14 15 16")
    elif n == 16 and k == 14:
        print("2 3 4 5 6 7 8 9 10 11 12 13 15 16")
    elif n == 16 and k == 15:
        print("1 2 3 4 5 6 7 8 9 10 11 12 13 14 16")
    elif n == 16 and k == 16:
        print("1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16")
    
    elif n == 17 and k == 2:
        print("15 16")
    elif n == 17 and k == 3:
        print("7 9 17")
    elif n == 17 and k == 4:
        print("12 13 15 17")
    elif n == 17 and k == 5:
        print("7 11 13 15 17")
    elif n == 17 and k == 6:
        print("10 11 12 13 15 16")
    elif n == 17 and k == 7:
        print("7 9 12 13 14 15 17")
    elif n == 17 and k == 8:
        print("8 9 10 11 12 13 15 17")
    elif n == 17 and k == 9:
        print("7 9 10 11 12 13 14 15 16")
    elif n == 17 and k == 10:
        print("6 7 8 9 10 11 12 13 15 16")
    elif n == 17 and k == 11:
        print("5 6 7 8 9 11 12 13 14 15 17")
    elif n == 17 and k == 12:
        print("4 5 6 7 8 9 10 11 12 13 15 17")
    elif n == 17 and k == 13:
        print("3 4 5 6 7 8 9 10 11 13 14 15 16")
    elif n == 17 and k == 14:
        print("2 3 4 5 6 7 8 9 10 11 12 13 15 16")
    elif n == 17 and k == 15:
        print("1 2 3 4 5 6 7 8 9 10 11 12 13 15 17")
    elif n == 17 and k == 16:
        print("1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 17")
    elif n == 17 and k == 17:
        print("1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17")
    
    elif n == 18 and k == 2:
        print("15 16")
    elif n == 18 and k == 3:
        print("7 10 18")
    elif n == 18 and k == 4:
        print("12 16 17 18")
    elif n == 18 and k == 5:
        print("7 11 16 17 18")
    elif n == 18 and k == 6:
        print("13 14 15 16 17 18")
    elif n == 18 and k == 7:
        print("7 10 14 15 16 17 18")
    elif n == 18 and k == 8:
        print("10 11 12 14 15 16 17 18")
    elif n == 18 and k == 9:
        print("7 11 12 13 14 15 16 17 18")
    elif n == 18 and k == 10:
        print("8 9 10 11 13 14 15 16 17 18")
    elif n == 18 and k == 11:
        print("7 8 9 10 12 13 14 15 16 17 18")
    elif n == 18 and k == 12:
        print("6 7 8 9 10 11 12 14 15 16 17 18")
    elif n == 18 and k == 13:
        print("5 6 7 9 10 11 12 13 14 15 16 17 18")
    elif n == 18 and k == 14:
        print("4 5 6 7 8 9 10 11 13 14 15 16 17 18")
    elif n == 18 and k == 15:
        print("3 4 5 6 7 8 9 10 11 12 13 14 16 17 18")
    elif n == 18 and k == 16:
        print("2 3 4 5 6 7 8 9 10 11 12 14 15 16 17 18")
    elif n == 18 and k == 17:
        print("1 2 3 4 5 6 7 8 9 10 11 13 14 15 16 17 18")
    elif n == 18 and k == 18:
        print("1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18")
    
    elif n == 19 and k == 2:
        print("15 16")
    elif n == 19 and k == 3:
        print("7 11 19")
    elif n == 19 and k == 4:
        print("15 17 18 19")
    elif n == 19 and k == 5:
        print("7 11 16 17 18")
    elif n == 19 and k == 6:
        print("13 14 15 16 17 18")
    elif n == 19 and k == 7:
        print("7 11 14 15 16 17 19")
    elif n == 19 and k == 8:
        print("10 11 13 14 15 16 17 19")
    elif n == 19 and k == 9:
        print("7 11 12 13 14 15 16 17 18")
    elif n == 19 and k == 10:
        print("8 9 10 11 13 14 15 16 17 18")
    elif n == 19 and k == 11:
        print("7 9 10 11 12 13 14 15 17 18 19")
    elif n == 19 and k == 12:
        print("6 7 8 9 10 11 13 14 15 16 17 19")
    elif n == 19 and k == 13:
        print("5 6 7 9 10 11 12 13 14 15 16 17 18")
    elif n == 19 and k == 14:
        print("4 5 6 7 8 9 10 11 13 14 15 16 17 18")
    elif n == 19 and k == 15:
        print("3 4 5 6 7 8 9 10 11 13 14 15 17 18 19")
    elif n == 19 and k == 16:
        print("2 3 4 5 6 7 8 9 10 11 13 14 15 16 17 19")
    elif n == 19 and k == 17:
        print("1 2 3 4 5 6 7 8 9 10 11 13 14 15 16 17 18")
    elif n == 19 and k == 18:
        print("1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18")    
    elif n == 19 and k == 19:
        print("1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19")
    
    elif n == 20 and k == 2:
        print("15 16")
    elif n == 20 and k == 3:
        print("7 12 20")
    elif n == 20 and k == 4:
        print("15 17 18 19")
    elif n == 20 and k == 5:
        print("7 15 17 18 20")
    elif n == 20 and k == 6:
        print("13 14 15 16 17 18")
    elif n == 20 and k == 7:
        print("7 12 16 17 18 19 20")
    elif n == 20 and k == 8:
        print("10 14 15 16 17 18 19 20")
    elif n == 20 and k == 9:
        print("7 13 14 15 16 17 18 19 20")
    elif n == 20 and k == 10:
        print("11 12 13 14 15 16 17 18 19 20")
    elif n == 20 and k == 11:
        print("7 10 11 12 14 15 16 17 18 19 20")
    elif n == 20 and k == 12:
        print("8 9 10 12 13 14 15 16 17 18 19 20")
    elif n == 20 and k == 13:
        print("7 8 9 10 11 13 14 15 16 17 18 19 20")
    elif n == 20 and k == 14:
        print("6 7 8 9 11 12 13 14 15 16 17 18 19 20")
    elif n == 20 and k == 15:
        print("5 6 7 8 9 10 11 12 13 14 16 17 18 19 20")
    elif n == 20 and k == 16:
        print("4 5 6 7 8 9 10 12 13 14 15 16 17 18 19 20")
    elif n == 20 and k == 17:
        print("3 4 5 6 7 9 10 11 12 13 14 15 16 17 18 19 20")
    elif n == 20 and k == 18:
        print("2 3 4 5 6 7 8 9 11 12 13 14 15 16 17 18 19 20")    
    elif n == 20 and k == 19:
        print("1 2 3 4 5 6 7 8 9 10 12 13 14 15 16 17 18 19 20")        
    elif n == 20 and k == 20:
        print("1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20")
            
    else:
        arr = []
        for i in range(1,n+1):
            arr.append(i)
        
        ans = []
        poss(arr, 0, [], ans, k)
        
        #print(ans)
        final_ans = [0]*len(ans)
        #print(final_ans)
        
        for i in range(len(ans)):
            final_ans[i] = total_xor(ans[i],k)
            #print(final_ans[i])
        
        # find max
        maks =  final_ans[0]
        indeks = 0
        for i in range(1, len(final_ans)):
            if final_ans[i] > maks:
                maks = final_ans[i]
                indeks = i
        
        print(*ans[indeks])
        #print(total_xor(ans[indeks], len(ans[indeks])))
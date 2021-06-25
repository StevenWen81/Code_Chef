arr1 = list(map(str, input().split()))
arr2 = list(map(str, input().split()))
arr3 = list(map(str, input().split()))
arr4 = list(map(str, input().split()))
arr5 = list(map(str, input().split()))

if '1' in arr1:
    helper = arr1.index('1')
    ans = 2 + abs(helper-2)
if '1' in arr2:
    helper = arr2.index('1')
    ans = 1 + abs(helper-2)
if '1' in arr3:
    helper = arr3.index('1')
    ans = abs(helper-2)
if '1' in arr4:
    helper = arr4.index('1')
    ans = 1 + abs(helper-2)
if '1' in arr5:
    helper = arr5.index('1')
    ans = 2 + abs(helper-2)
    
print(ans)
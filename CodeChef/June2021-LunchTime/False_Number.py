t = int(input())
for i in range(t):
    ans = ""
    num = str(input())
    if num[0] == '1':
        ans += num[0] + '0'
        ans += num[1:]
    else:
        ans += '1' + num
    print(ans)
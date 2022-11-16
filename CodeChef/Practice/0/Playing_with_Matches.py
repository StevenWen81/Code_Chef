# 100/100
t = int(input())

for i in range(t):
    s,w = map(int, input().split())
    total = s+w
    total = str(total)
    
    ans = 0
    
    for i in range(len(total)):
        if total[i] == "0":
            ans += 6
        if total[i] == "1":
            ans += 2
        if total[i] == "2":
            ans += 5
        if total[i] == "3":
            ans += 5
        if total[i] == "4":
            ans += 4
        if total[i] == "5":
            ans += 5
        if total[i] == "6":
            ans += 6
        if total[i] == "7":
            ans += 3
        if total[i] == "8":
            ans += 7
        if total[i] == "9":
            ans += 6
    
    print(ans)
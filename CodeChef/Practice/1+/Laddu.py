for _ in range(int(input())):
    l,nation = input().split()
    ans = 0
    for i in range(int(l)):
        task = input().split()
        if task[0] == "CONTEST_WON":
            rank = int(task[1])
            ans+=300 + max(20-rank,0)
        if task[0] == "TOP_CONTRIBUTOR":
            ans+=300
        if task[0] == "BUG_FOUND":
            ans+=int(task[1])
        if task[0] == "CONTEST_HOSTED":
            ans+=50
    if nation == "INDIAN":
        print(ans//200)
    else:
        print(ans//400)
t = int(input())

for i in range(t):
    stud, chair = map(int, input().split())

    ans = 0
    if stud > chair:
        ans = stud-chair
    
    print(ans)
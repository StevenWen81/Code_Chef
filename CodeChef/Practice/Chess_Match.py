t = int(input())

for i in range(t):
    a,b,c = map(int, input().split())
    time = 2 * (180+a)
    print(time-b-c)
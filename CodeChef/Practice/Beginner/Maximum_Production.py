t = int(input())

for i in range(t):
    d, x, y, z = list(map(int, input().split()))
    hold1 = x * 7
    hold2 = d*y + (7-d)*z
    
    print(max(hold1, hold2))
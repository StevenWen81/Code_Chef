t = int(input())

for i in range(t):
    start, want = map(int, input().split())

    if start <= want <= start + 200:
        print("YES")
    else:
        print("NO")
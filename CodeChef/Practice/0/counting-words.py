t = int(input())

for i in range(t):
    page, word = map(int, input().split())

    print(page * word)
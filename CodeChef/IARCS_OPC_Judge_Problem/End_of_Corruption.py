minister, king = map(int, input().split())
t = minister + king
store = []
for i in range(t):
    x = int(input())
    if x == -1:
        store.sort()
        ans = len(store)-1
        print(store[ans])
        store.pop(ans)
    else:
        if len(store) > 0:
            if x < store[0]:
                store.insert(0,x)
            else:
                store.append(x)
        else:
            store.append(x)
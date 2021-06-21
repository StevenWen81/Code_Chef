t = int(input())
arr = []
for i in range(t):
    x = int(input())
    arr.append(x)
arr.sort()

ans = []
n = 0
for i in arr:
    gain = i * (len(arr) - n)
    ans.append(gain)
    n += 1
print(max(ans))
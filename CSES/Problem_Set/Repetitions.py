dna = str(input())

start = dna[0]
count = 1
ans = 1

for i in dna[1:]:
    if i == start:
        count += 1
    else:
        start = i
        ans = max(ans, count)
        count = 1
print(max(ans,count))
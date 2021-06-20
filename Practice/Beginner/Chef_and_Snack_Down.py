# 100/100
t = int(input())
arr = [2010, 2015, 2016, 2017, 2019]

for i in range(t):
    year = int(input())
    if year in arr:
        print("HOSTED")
    else:
        print("NOT HOSTED")
t = int(input())

for i in range(t):
    rtp, audit, non = map(int, input().split())

    print(rtp*4 + audit*2)
def reset(x):
    x = 0
    return x

vowel = ["a", "i", "u", "e", "o"]

t = int(input())

for i in range(t):
    l = int(input())
    s = str(input())

    streak_consonant = 0

    easy = "YES"
    for i in s:
        if i in vowel:
            streak_consonant = reset(streak_consonant)
        else:
            streak_consonant += 1
            if streak_consonant > 3:
                easy = "NO"

    print(easy)

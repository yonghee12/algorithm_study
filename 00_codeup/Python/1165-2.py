array = input().strip().split(" ")
time, score = list(map(int, array))

def func(time, score):
    rest = 90 - time
    if rest % 5 == 0:
        return score + rest//5
    else:
        return score + rest//5 + 1

print(func(time, score))
array = input().strip().split(" ")
time, score = list(map(int, array))

def func(time, score):
    count = 0
    for i in range(time, 90, 5):
        count += 1
    return score + count

print(func(time, score))
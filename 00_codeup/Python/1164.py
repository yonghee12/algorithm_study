array = input().strip().split(" ")
array = list(map(int, array))

def f(array):
    for item in array:
        if item <= 170:
            return "CRASH"
    return "PASS"

print(f(array))
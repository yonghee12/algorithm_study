a, b = input().strip().split(" ")
a, b = int(a), int(b)

calcs = []
biggest = a + b

funcs = [
    # lambda x, y : x + y,
    lambda x, y : x - y,
    lambda x, y : y - x,
    lambda x, y : x * y,
    lambda x, y : x / y,
    lambda x, y : y / x,
    lambda x, y : x**y,
    lambda x, y : y**x
]

for func in funcs:
    if biggest < func(a, b):
        biggest = func(a, b)

print("{:6f}".format(biggest))
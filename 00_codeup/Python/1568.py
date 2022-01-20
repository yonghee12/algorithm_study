def f(array, a, b):
    biggest = -2147483648
    biggest_index = 0
    for i in range(a-1, b, 1):
        if array[i] > biggest:
            biggest = array[i]
            biggest_index = i
    return biggest_index + 1

n = int(input().strip())
array = input().strip().split(" ")
a, b = input().strip().split(" ")
a, b = int(a), int(b)

for i in range(0, n, 1):
    array[i] = int(array[i])

print(f(array, a, b))
def f(n, array, k):
    position = -1
    for i in range(0, n, 1):
        if array[i] == k:
            position = i + 1
            break
    return position

n = int(input())
array = input().strip().split(" ")
for i in range(0, n, 1):
    array[i] = int(array[i])

k = int(input())

print(f(n, array, k))
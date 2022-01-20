# n = int(input())
# ​
# for i in range(0, n):
#     for j in range(1, n+1):
#         print(n*i+j, end=' ')
#     print()

n = int(input())
arr = []
number = 1

for i in range(n):
    arr.append([])
    for j in range(n):
        arr[i].append(number)
        number += 1

for i in range(n):
    arr.append([])
    for j in range(n):
        print(arr[i][j], end=' ')
    print()
array = input().strip().split(" ")

for i in range(0, len(array), 1):
    array[i] = int(array[i])

# 여기부터 함수


# 1번
def f1(array):
    n = len(array)
    result = []
    temp = 0
    for i in range(0, n, 1):
        temp = array[i]
        is_same = False
        for j in range(0, len(result), 1):
            if temp == result[j]:
                is_same = True
        if not is_same:
            result.append(temp)
    return result


# 2번
def f2(array):
    n = len(array)
    result = []
    temp = 0
    for i in range(0, n, 1):
        if array[i] not in result:
            result.append(array[i])
    return result

# 3번
def f3(array):
    return list(set(result))

print(f(array))
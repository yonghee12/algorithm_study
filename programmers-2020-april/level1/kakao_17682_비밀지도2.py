# https://programmers.co.kr/learn/courses/30/lessons/17681
"""
Lesson
string manipulation시 list comp, map보다 그 이전에 아예 한 번에 풀릴 상황을 생각해보라
"""


arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

arr1 = [46, 33, 33, 22, 31, 50]
arr2 = [27, 56, 19, 14, 14, 10]


def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        code = bin(i | j)[2:]
        code = code.zfill(n)
        code = code.replace('1', '#')
        code = code.replace('0', ' ')
        answer.append(code)
    return answer


solution(6, arr1, arr2)


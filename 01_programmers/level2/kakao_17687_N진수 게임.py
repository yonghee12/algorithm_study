# https://programmers.co.kr/learn/courses/30/lessons/17687
"""
일단
"""

from collections import deque

def change_system(decimal, n):
    fillers = "0123456789ABCDEF"
    q, r = divmod(decimal, n)
    if q == 0:
        return fillers[r]
    else:
        return change_system(q, n) + fillers[r]


def solution(n, t, m, p):
    numbers = []
    answer = ''
    answer_range = deque(range(p-1, t*m + p, m))
    i = 0
    j = answer_range.popleft()
    while True:
        numbers.extend(list(str(change_system(i, n))))
        if len(numbers) > j:
            answer += numbers[j]
            j = answer_range.popleft()
        if len(answer) == t:
            return answer
        i += 1


solution(16, 16, 2, 1)

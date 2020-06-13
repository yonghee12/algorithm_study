# https://programmers.co.kr/learn/courses/30/lessons/42889
from collections import Counter
from operator import itemgetter

"""
Lessons
agg를 생각했다면 뺄셈도 생각해보자!
뺄셈으로서 counter 이후에 for 문 한 번만 돌아도 된다.
"""

def solution(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)


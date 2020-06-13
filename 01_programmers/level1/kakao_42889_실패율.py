# https://programmers.co.kr/learn/courses/30/lessons/42889
'''
정답률 55.75%
'''

from collections import Counter
from operator import itemgetter

def solution(N: int, stages: list):
    counter = Counter(stages)
    reached_agg = {stage: 0 for stage in range(1, N+1)}
    reached_agg[N+1] = counter[N+1]
    for i in range(N, 0, -1):
        reached_agg[i] = reached_agg[i+1] + counter[i]

    fail_rates = []
    for i in range(1, N+1):
        fail_rate = counter[i] / reached_agg[i] if reached_agg[i] != 0 else 0
        fail_rates.append((i, fail_rate))

    fail_rates_sort = sorted(fail_rates, key=itemgetter(1), reverse=True)
    return [fail_rate[0] for fail_rate in fail_rates_sort]

solution(4, [1,1,1])
solution(5, [2, 1, 2, 6, 2, 4, 3, 3])



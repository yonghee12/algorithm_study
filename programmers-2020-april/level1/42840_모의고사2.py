# https://programmers.co.kr/learn/courses/30/lessons/42840
"""
Lesson Learned
어짜피 3n일거면 더 간결하게 표현되는 것이 낫다.
바깥 for문이 더 긴 게 보기 좋은듯.
modular 잘 생각함.
idx 1을 위해 dict를 쓸 필요는 없는 것 같다. 그냥 리스트 쓰자.
세명이라 max 썼지만 과연..?
"""

def solution(answers):
    students = {1: [1, 2, 3, 4, 5],
                2: [2, 1, 2, 3, 2, 4, 2, 5],
                3: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]}
    scores = {1: 0, 2: 0, 3: 0}

    for idx, ans in enumerate(answers):
        for s_num, series in students.items():
            if series[idx % len(series)] == ans:
                scores[s_num] += 1

    max_score = max(scores.values())
    return [s_num for s_num, score in scores.items() if score == max_score]


solution([1, 2, 3, 4, 5])
solution([1, 3, 2, 4, 2])

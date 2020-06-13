# https://programmers.co.kr/learn/courses/30/lessons/42840

students = [[1, 2, 3, 4, 5],
            [2, 1, 2, 3, 2, 4, 2, 5],
            [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]


def check_answer(student, answers):
    score = 0
    for idx, ans in enumerate(answers):
        if student[idx % len(student)] == ans:
            score += 1
    return score


def solution(answers):
    answer = []
    high_score = 0
    for idx, student in enumerate(students):
        score = check_answer(student, answers)
        if score > high_score:
            answer = [idx + 1]
            high_score = score
        elif score == high_score:
            answer.append(idx + 1)
    return answer


solution([1,2,3,4,5])

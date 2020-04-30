# https://programmers.co.kr/learn/courses/30/lessons/17682

def solution(result):
    bonuses = {"S": lambda x: x,
               "D": lambda x: x ** 2,
               "T": lambda x: x ** 3, }
    scores = list()
    score_stack = list()
    for r in result:
        if r in '0123456789':
            score_stack.append(r)
        elif r in "SDT":
            score = int(''.join(score_stack))
            scores.append(bonuses[r](score))
            score_stack = list()
        elif r == "*":
            for i in range(len(scores) - 1, -1, -1)[:2]:
                scores[i] = scores[i] * 2
        else:
            scores[len(scores) - 1] = scores[len(scores) - 1] * (-1)
    return sum(scores)


tc = ['1S2D*3T', '1D2S#10S', '1D2S0T', '1S*2T*3S', '1D#2S*3S', '1T2D3D#', '1D2S3T*']
for t in tc:
    print(solution(t))

# Short Answer
import re


def solution(result):
    bonus = {'S': 1, 'D': 2, 'T': 3}
    option = {'': 1, '*': 2, '#': -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(result)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i - 1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer

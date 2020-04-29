# https://programmers.co.kr/learn/courses/30/lessons/17682
import re

result = "1S2D*3T"


def solution(result):
    metrics = {"S": lambda x: x,
               "D": lambda x: x ** 2,
               "T": lambda x: x ** 3, }
    scores = list()
    for r in result:
        if re.findall('\d', r):
            scores.append(int(r))
            idx = len(scores) - 1
        elif re.findall("[A-Z]", r):
            scores[idx] = metrics[r](scores[idx])
        elif r == '*':
            scores[idx] = scores[idx] * 2
            scores[idx-1] = scores[idx-1] * 2
        else:
            scores[idx] = scores[idx] * (-1)
    return sum(scores)

tc = ['1D2S#10S', '1S*2T*3S']
for t in tc:
    print(solution(t))
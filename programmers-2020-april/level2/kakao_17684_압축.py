# https://programmers.co.kr/learn/courses/30/lessons/17684
# 40

from string import ascii_uppercase
dic = {upper: i+1 for i, upper in enumerate(ascii_uppercase)}

def process(text, stack=''):
    if not text:
        return dic[stack], text
    else:
        stack += text[0]
        text = text[1:]
        if stack not in dic.keys():
            dic[stack] = len(dic) + 1
            return dic[stack[:-1]], stack[-1] + text
        else:
            return process(text, stack)


def solution(msg):
    answer = []
    text = msg[:]
    while True:
        res, text = process(text)
        answer.append(res)
        if not text:
            return answer

msg = "TOBEORNOTTOBEORTOBEORNOT"
# msg = "KAKAO"
msg = "ABABABABABABABAB"
solution(msg)

# 더러운 풀이지만....
# 다시 짠다면 재귀 안쓰고 while만 써서 짤 수도 있을듯!

def solution(msg):
    answer = []
    tmp = {chr(e + 64): e for e in range(1, 27)}
    num = 27
    while msg:
        tt = 1
        while msg[:tt] in tmp.keys() and tt <= msg.__len__():
            tt += 1
        tt -= 1
        if msg[:tt] in tmp.keys():
            answer.append(tmp[msg[:tt]])
            tmp[msg[:tt + 1]] = num
            num += 1
        msg = msg[tt:]
    return answer
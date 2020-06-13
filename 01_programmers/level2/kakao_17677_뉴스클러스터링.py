# https://programmers.co.kr/learn/courses/30/lessons/17677
'''
정답률 41.84%
소요시간 25분
낮은 정답률에 비해 쉽게 풀었지만 그것은 파이썬이라서 그런 것 같다.
set과 counter가 존재해서 쉬웠지만 다른 언어를 잡았다면 시간이 더 걸렸을듯
아마 element-wise로 for문 사용하여 검사하고 counter를 직접 구현했을 것 같다.

나머지 파이썬 유저들도 비슷하게 풀은듯.
중복 허용하지 않는 집합 : set
중복 허용하는 집합 : Counter

이것 기억
'''


from collections import Counter
from string import ascii_lowercase as lo, ascii_uppercase as up
alphabets = lo + up

def bigram(text):
    return [text[i:i+2].lower() for i in range(len(text)-1)
            if text[i] in alphabets and text[i+1] in alphabets]

def solution(str1, str2):
    s1, s2 = map(bigram, [str1, str2])
    c1, c2 = Counter(s1), Counter(s2)
    inter, union = c1 & c2, c1 | c2
    val = sum(inter.values()) / sum(union.values()) if union.values() else 1
    return int(val * 65536)

string = ('FRANCE', 'french')
string = ["handshake", "shake hands"]
string = ['aa1+aa2', 'AAAA12']
string = ['E=M*C^2', 'e=m*c^2']
solution(*string)
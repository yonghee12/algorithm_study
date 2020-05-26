# https://programmers.co.kr/learn/courses/30/lessons/60057

def ngram(s, n):
    if n == 1:
        return list(s)
    ngrams = []
    for i in range(0, len(s), n):
        ngrams.append(s[i:i + n])
    return ngrams

def comp(s, n):
    ngrams = ngram(s, n)
    bag = [ngrams[0]]
    res = ''
    for token in ngrams[1:]:
        if token == bag[-1]:
            bag.append(token)
        else:
            length = str(len(bag)) if len(bag) > 1 else ''
            res += length + bag[0]
            bag = [token]
    length = str(len(bag)) if len(bag) > 1 else ''
    res += length + bag[0]

    return res


def solution(s):
    smallest = len(s)
    for n in range(1, len(s)):
        comp_l = len(comp(s, n))
        smallest = comp_l if smallest > comp_l else smallest
    return smallest


strings = [
    "aabbaccc",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd"
]
for s in strings:
    print(solution(s))


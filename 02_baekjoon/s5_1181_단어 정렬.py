# https://acmicpc.net/problem/1181
"""
쉬운 문제지만 두 가지 lesson learned
1. 연산이 적은 문제의 경우 input 시간이 중요하다. input 많을수록 sys.stdin
2. 두 가지 key로 sort할 경우 두 번 따로 sort하는게 낫다.
"""


import sys
input = sys.stdin.readline

n = int(input().rstrip())
s = set()
for _ in range(n):
    s.add(input().rstrip())
l = list(s)
l.sort()
l.sort(key=lambda x: len(x), reverse=False)
print('\n'.join(l))
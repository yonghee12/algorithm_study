# 세 변의 길이가 같은 경우 : 정삼각형

# 두 변의 길이가 같은 경우 : 이등변삼각형

# a2 + b2 = c2일 경우(피타고라스 정리) : 직각삼각형

# 위의 조건에 맞지 않는 일반 삼각형일 경우 : 삼각형

# 삼각형이 아닐 경우 : 삼각형아님

import sys

a, b, c = input().strip().split(" ")
a, b, c = int(a), int(b), int(c)

def f(a, b, c):
    if a + b <= c:
        return "삼각형아님"
    elif a==b and b==c:
        return "정삼각형"
    elif a==b or b==c:
        return "이등변삼각형"
    elif a**2 + b**2 == c**2:
        return "직각삼각형"
    else:
        return "삼각형"

sys.stdout.write(f(a,b,c))
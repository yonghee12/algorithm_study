# https://www.acmicpc.net/problem/9935
import sys

input = sys.stdin.readline

string = input().strip()
bomb = input().strip()
leng = len(bomb)
end = len(string) - len(bomb)


def check(string, bomb, start_i):
    for j in range(leng):
        i = start_i + j
        if i > len(string) - 1:
            return False
        if string[start_i + j] != bomb[j]:
            return False
    return True


ans = ''
i = 0
flag = False
while True:
    if not check(string, bomb, i) or i > end:
        ans += string[i]
        if flag and len(ans) - leng >= 0:
            if check(ans, bomb, len(ans) - leng):
                ans = ans[:-leng]
                flag = False
        i += 1
        if i > len(string) - 1:
            break
    else:
        i += leng
        flag = True

ans = ans if ans else "FRULA"
print(ans)

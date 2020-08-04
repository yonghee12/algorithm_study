# https://www.acmicpc.net/problem/9935

string = input()
bomb = input()
bombl = list(bomb)
b_last = bomb[-1]
bl = len(bomb)

ans = []
for l in string:
    ans.append(l)
    if b_last == l and bombl == ans[-bl:]:
        del ans[-bl:]

print(''.join(ans) if ans else "FRULA")
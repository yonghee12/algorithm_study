# # https://www.acmicpc.net/problem/1920

import sys


def read():
    return sys.stdin.readline().strip()


n = int(read())
a = read().split(' ')
m = int(read())
b = read().split(' ')

dic = {k: 1 for k in a}
sys.stdout.write('\n'.join([str(int(k in dic)) for k in b]))


def main():
    input()
    n = input().strip().split(' ')
    input()

    s = set(n)
    r = ''
    for k in input().strip().split(' '):
        r += '1\n' if k in s else '0\n'
    print(r)

main()

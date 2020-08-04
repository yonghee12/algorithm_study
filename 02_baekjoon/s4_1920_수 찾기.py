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
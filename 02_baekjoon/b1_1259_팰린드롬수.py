# https://www.acmicpc.net/problem/1259
import sys


def check(word):
    l = len(word)
    for i in range(l // 2):
        if word[i] != word[l - i - 1]:
            return 'no'
    return 'yes'


def main():
    while True:
        w = sys.stdin.readline().rstrip()
        if w == '0':
            break
        print(check(w))


if __name__ == '__main__':
    main()

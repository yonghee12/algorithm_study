# https://www.acmicpc.net/problem/10818

import sys
input = sys.stdin.readline

def main():
    input()
    arr = map(int, input().split())
    min, max = 1000000, -1000000
    for n in arr:
        max = n if n > max else max
        min = n if n < min else min
    print(min, max)

if __name__ == '__main__':
    main()
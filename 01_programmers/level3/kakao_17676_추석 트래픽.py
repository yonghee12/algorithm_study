# https://programmers.co.kr/learn/courses/30/lessons/17676

from datetime import datetime as dt
from collections import deque
import sys

sys.setrecursionlimit(100000000)


def parsetime(time):
    hms, ms = time.split(".")
    hms = list(map(int, hms.split(":")))
    multiple = (1000, 60000, 3600000)
    hms_ms = 0
    for i in range(3):
        hms_ms += hms.pop() * multiple[i]
    return hms_ms + int(ms)


def parse(line):
    end, dur = line.split(' ')[1:]
    end = parsetime(end)
    dur = int(float(dur[:-1]) * 1000)
    start = end - dur + 1
    start = 0 if start < 0 else start
    return (start, end)




def solution(lines):
    parsed = [parse(line) for line in lines]
    if len(parsed) <= 1:
        return 1
    minimum = sorted(parsed, key=lambda x: x[0], reverse=False)[0][0]
    maximum = sorted(parsed, key=lambda x: x[1], reverse=True)[0][1]
    bound = maximum - minimum
    parsed = [(l[0] - minimum, l[1] - minimum) for l in parsed]

    arr = [[0 for _ in range(bound + 1)]
           for _ in range(len(lines))]
    for i, l in enumerate(parsed):
        for j in range(l[0], l[1] + 1):
            arr[i][j] = 1

    biggest = 0
    for a, b in parsed:
        for k in [a-1, a, a+1, b-1, b, b+1]:
            lines = 0
            for i in range(0, len(arr)):
                get = arr[i][k:k + 1000]
                if get:
                    if max(get):
                        lines += 1
            if lines > biggest:
                biggest = lines
    biggest
    return biggest


lines = ["2016-09-15 20:59:57.421 0.351s",
         "2016-09-15 20:59:58.233 1.181s",
         "2016-09-15 20:59:58.299 0.8s",
         "2016-09-15 20:59:58.688 1.041s",
         "2016-09-15 20:59:59.591 1.412s",
         "2016-09-15 21:00:00.464 1.466s",
         "2016-09-15 21:00:00.741 1.581s",
         "2016-09-15 21:00:00.748 2.31s",
         "2016-09-15 21:00:00.966 0.381s",
         "2016-09-15 21:00:02.066 2.62s"
]
if __name__ == '__main__':
    print(solution(lines))

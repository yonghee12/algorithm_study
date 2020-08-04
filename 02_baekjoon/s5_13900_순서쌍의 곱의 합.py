# https://www.acmicpc.net/problem/13900
import sys
input = sys.stdin.readline

input()
nums = list(map(int, input().strip().split(' ')))
s = sum(nums)
ans = 0
for n in nums:
    s = s - n
    ans += n * s

print(ans)
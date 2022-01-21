# https://www.acmicpc.net/problem/2798

N, M = map(int, input().strip().split())
nums = sorted(list(map(int, input().strip().split())))

blackjack = 0
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        middle = nums[i] + nums[j]
        if middle > M:
            continue
        for k in range(j + 1, len(nums)):
            final = middle + nums[k]
            if final > M:
                break
            blackjack = final if final > blackjack else blackjack
print(blackjack)
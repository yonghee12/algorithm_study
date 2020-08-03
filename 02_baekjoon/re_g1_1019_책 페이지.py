n = int(input().strip())
nums = {str(k): 0 for k in range(10)}
for i in range(1, n + 1):
    for l in str(i):
        nums[l] += 1
print(' '.join([str(nums[str(i)]) for i in range(10)]))
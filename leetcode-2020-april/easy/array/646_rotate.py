# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/
# TODO: 다시보기

def rotate(nums: list, k: int):
    nums.reverse()
    for _ in range(k):
        nums.append(nums.pop(0))
    nums.reverse()
    return nums

rotate([1, 2, 3, 4, 5, 6, 7], 3)

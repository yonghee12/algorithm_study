# https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/578/
'''
여기서 1번은 O(n), 2번은 O(nlogn)이지만 개수에 따라 1이 더 느릴수도 있다.
3번은 트릭
'''

def containsDuplicate(nums: list) -> bool:
    cache = dict()
    for n in nums:
        if cache.get(n):
            return True
        cache[n] = True
    return False


def containsDuplicate2(nums: list) -> bool:
    nums = sorted(nums)
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False


def containsDuplicate3(nums: list) -> bool:
    if len(set(nums)) != len(nums) and len(nums):
        return True
    else:
        return False


containsDuplicate3([1, 2, 3, 3])

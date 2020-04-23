def removeDuplicates(nums) -> int:
    if not nums:
        return 0
    elif len(nums) == 1:
        return 1
    else:
        i = 0
        while True:
            while True:
                if nums[i] == nums[i+1]:
                    nums.pop(i+1)
                    if i >= len(nums) - 1:
                        break
                else:
                    break
            i += 1
            if i >= len(nums)-1:
                break
        return len(nums)

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(removeDuplicates([1]))
print(removeDuplicates(nums))

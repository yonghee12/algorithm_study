def removeDuplicates(nums) -> int:
    if not nums:
        return 0
    else:
        j = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
        return j + 1


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

print(removeDuplicates(nums))
print(removeDuplicates([]))
print(removeDuplicates([1]))
print(removeDuplicates([1, 1]))
print(removeDuplicates([1, 1, 1]))
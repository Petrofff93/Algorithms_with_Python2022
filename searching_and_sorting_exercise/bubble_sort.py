nums = [1, 3, 4, 2, 5, 6]

for i in range(len(nums)):
    for j in range(1, len(nums)):
        if nums[j - 1] > nums[j]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]

print(nums)


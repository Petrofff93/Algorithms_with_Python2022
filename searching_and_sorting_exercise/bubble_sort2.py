nums = [1, 3, 4, 2, 5, 6]
is_sorted = False
i = 0
while not is_sorted:
    is_sorted = True
    for j in range(1, len(nums) - 1):
        if nums[j - 1] > nums[j]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            is_sorted = False
    i += 1

print(nums)

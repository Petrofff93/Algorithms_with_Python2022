nums = [3, 2, 4, 6, 8, 7, 1, 5]

for idx in range(len(nums)):
    min_idx = idx
    for current_idx in range(idx + 1, len(nums)):
        if nums[current_idx] < nums[min_idx]:
            min_idx = current_idx
    nums[idx], nums[min_idx] = nums[min_idx], nums[idx]

print(nums)


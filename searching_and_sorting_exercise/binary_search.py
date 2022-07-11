def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1
    while left <= right:
        mid_idx = (left + right) // 2
        mid_el = numbers[mid_idx]
        if mid_el == target:
            return mid_idx
        if mid_el < target:
            left = mid_idx + 1
        else:
            right = mid_idx - 1
    return -1


nums = [1, 2, 3, 4, 5, 6, 7]
t = 5
print(binary_search(nums, t))


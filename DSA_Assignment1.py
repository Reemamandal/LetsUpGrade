def majority_element(nums):
    count = 1
    candidate = nums[0]

    for i in range(1, len(nums)):
        if nums[i] == candidate:
            count += 1
        else:
            count -= 1
            if count == 0:
                candidate = nums[i]
                count = 1

    # Verify if the candidate appears more than n/2 times
    count = 0
    for num in nums:
        if num == candidate:
            count += 1
    if count > len(nums) // 2:
        return candidate
    else:
        return -1

# Test case
nums = [2, 4, 5, 5, 5, 5, 5]
result = majority_element(nums)
print(result)  # Output: 5
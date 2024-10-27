def two_sum(nums, target):
    seen = set()
    for num in nums:
        complement = target - num
        if complement in seen:
            return True
        seen.add(num)
    return False

# Test: Provide a list of numbers and a target sum
nums = [2, 7, 11, 15]
target = 9
print(f"Two numbers in {nums} add up to {target}: {two_sum(nums, target)}")

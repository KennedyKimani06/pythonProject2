def sum_of_list(nums):
    total = 0
    for num in nums:
        total += num
    return total

# Test: Provide a list of numbers
nums = [1, 2, 3, 4, 5]
print(f"The sum of {nums} is: {sum_of_list(nums)}")

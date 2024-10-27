def largest_in_tuple(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

# Test: Provide a tuple of numbers
numbers = (10, 20, 30, 40, 50)
print(f"Largest number in {numbers} is: {largest_in_tuple(numbers)}")

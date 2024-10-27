def keys_greater_than_n(d, n):
    return [key for key, value in d.items() if value > n]

# Test: Provide a dictionary and a threshold
d = {'a': 5, 'b': 12, 'c': 3}
n = 4
print(f"Keys with values greater than {n}: {keys_greater_than_n(d, n)}")

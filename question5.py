def print_even_value_keys(d):
    for key, value in d.items():
        if value % 2 == 0:
            print(f"Key with even value: {key}")

# Test: Provide a dictionary
d = {'a': 2, 'b': 3, 'c': 4}
print_even_value_keys(d)

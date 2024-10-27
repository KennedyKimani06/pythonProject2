def tuples_to_dict(tuples_list):
    return {key: value for key, value in tuples_list}

# Test: Provide a list of tuples
tuples_list = [("apple", 5), ("banana", 7), ("cherry", 3)]
print(f"Converted dictionary: {tuples_to_dict(tuples_list)}")

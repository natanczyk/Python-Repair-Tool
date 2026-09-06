def sort_age(lst):
    # Sort the list of tuples based on the second element (age) in descending order
    return sorted(lst, key=lambda x: x[1], reverse=True)
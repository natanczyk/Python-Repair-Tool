def sort_age(lst):
    # Use Python's built-in sorted function with a key that sorts by age in descending order
    return sorted(lst, key=lambda x: x[1], reverse=True)
def sort_age(lst):
    # Sort the list by age in descending order
    # We use a stable sort, but since ages are unique, stability doesn't matter for correctness
    # We sort by the second element of each tuple (age) in reverse order
    return sorted(lst, key=lambda x: x[1], reverse=True)
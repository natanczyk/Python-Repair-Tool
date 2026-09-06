def sort_age(lst):
    # Sort by age in descending order
    return sorted(lst, key=lambda x: x[1], reverse=True)
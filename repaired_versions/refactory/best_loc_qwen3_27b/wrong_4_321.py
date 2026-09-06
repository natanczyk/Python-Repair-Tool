def sort_age(lst):
    # Sort the list by age in descending order
    # We use a key that extracts the age (index 1) from each tuple
    # and reverse=True to get descending order (oldest first)
    return sorted(lst, key=lambda x: x[1], reverse=True)
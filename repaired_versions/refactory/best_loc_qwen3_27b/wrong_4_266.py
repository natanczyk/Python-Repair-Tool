def sort_age(lst):
    # Sort by age in descending order (older people at the front)
    # We use sorted() with a key that extracts the age (index 1) and reverse=True
    return sorted(lst, key=lambda x: x[1], reverse=True)
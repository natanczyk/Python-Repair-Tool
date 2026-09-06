def sort_age(lst):
    # Sort the list by age (second element of tuple) in descending order
    # We create a new sorted list to avoid modifying the original if needed,
    # but since the tests expect a returned list, we can sort in place or create new.
    # Using sorted() with a key to sort by age descending.
    return sorted(lst, key=lambda x: x[1], reverse=True)
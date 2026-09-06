def sort_age(lst):
    # Use the built-in sorted function with a custom key.
    # The key x[1] targets the age (the second element of the tuple).
    # reverse=True ensures the list is sorted in descending order (older people first).
    return sorted(lst, key=lambda x: x[1], reverse=True)
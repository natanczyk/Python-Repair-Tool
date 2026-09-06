def sort_age(lst):
    # The goal is to sort the list of tuples (gender, age) in descending order based on age.
    # We can use Python's built-in sorted function with a custom key.
    # The key lambda x: x[1] tells Python to sort based on the second element of the tuple (the age).
    # reverse=True ensures the sorting is in descending order (older people first).
    return sorted(lst, key=lambda x: x[1], reverse=True)
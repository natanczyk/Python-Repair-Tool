def sort_age(lst):
    # The goal is to sort the list of tuples (<gender>, <age>) 
    # in descending order based on the age (the second element of the tuple).
    # We can use Python's built-in sorted function with a custom key.
    return sorted(lst, key=lambda x: x[1], reverse=True)
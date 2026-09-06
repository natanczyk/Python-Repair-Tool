def sort_age(lst):
    # The goal is to sort the list of tuples (<gender>, <age>) 
    # such that the older people (higher age) are at the front.
    # We can use Python's built-in sorted function with a custom key.
    # The key will be the second element of the tuple (index 1), 
    # and reverse=True will ensure descending order.
    return sorted(lst, key=lambda x: x[1], reverse=True)
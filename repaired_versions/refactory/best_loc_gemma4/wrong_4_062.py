def sort_age(lst):
    # The goal is to sort the list of tuples (<gender>, <age>) 
    # such that the older people are at the front.
    # We can use Python's built-in sorted function with a custom key.
    # The key is the second element of the tuple (index 1), and reverse=True 
    # ensures descending order (older people first).
    return sorted(lst, key=lambda x: x[1], reverse=True)
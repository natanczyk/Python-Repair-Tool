def sort_age(lst):
    # The goal is to sort the list of tuples (<gender>, <age>) 
    # such that the older people (higher age) are at the front.
    # We can use Python's built-in sorted function with a custom key.
    # The key lambda x: x[1] extracts the age, and reverse=True sorts it descending.
    return sorted(lst, key=lambda x: x[1], reverse=True)
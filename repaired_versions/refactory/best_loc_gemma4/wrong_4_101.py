def sort_age(lst):
    # The goal is to sort the list of tuples (<gender>, <age>) 
    # such that the older people (higher age) are at the front.
    # We can use Python's built-in sorted function with a custom key.
    # lst[i][1] refers to the age of the person.
    return sorted(lst, key=lambda x: x[1], reverse=True)
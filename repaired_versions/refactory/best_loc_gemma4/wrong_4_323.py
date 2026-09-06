def sort_age(lst):
    # The goal is to sort the list of tuples (<gender>, <age>) 
    # by age in descending order.
    # We can use Python's built-in sorted function with a custom key.
    # The key lambda x: x[1] extracts the age, and reverse=True ensures descending order.
    return sorted(lst, key=lambda x: x[1], reverse=True)
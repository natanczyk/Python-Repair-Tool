def sort_age(lst):
    # The goal is to sort the list of tuples (gender, age) by age in descending order.
    # We can use Python's built-in sorted function with a custom key.
    # The key lambda x: x[1] tells Python to sort based on the second element of the tuple (the age).
    # reverse=True ensures that the older people (larger age) are at the front.
    return sorted(lst, key=lambda x: x[1], reverse=True)
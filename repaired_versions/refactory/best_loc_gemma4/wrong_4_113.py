def sort_age(lst):
    # The goal is to sort tuples of (gender, age) by age in descending order.
    # We can use Python's built-in sorted function with a custom key.
    # The key lambda x: x[1] extracts the age from the tuple.
    # reverse=True ensures that older people (higher age) are at the front.
    return sorted(lst, key=lambda x: x[1], reverse=True)
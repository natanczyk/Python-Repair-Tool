def sort_age(lst):
    # The goal is to sort the list of tuples (<gender>, <age>) 
    # such that the older people (higher age) are at the front.
    # We use the sorted() function with a custom key that targets the second element of the tuple (index 1).
    # reverse=True ensures the sorting is in descending order.
    return sorted(lst, key=lambda x: x[1], reverse=True)
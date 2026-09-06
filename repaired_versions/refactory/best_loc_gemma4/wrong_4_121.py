def sort_age(lst):
    # The goal is to sort the list of tuples by the second element (age) in descending order.
    # We use the sorted() function with a custom key that targets the age (index 1 of the tuple).
    # reverse=True ensures the older people are at the front of the list.
    return sorted(lst, key=lambda x: x[1], reverse=True)
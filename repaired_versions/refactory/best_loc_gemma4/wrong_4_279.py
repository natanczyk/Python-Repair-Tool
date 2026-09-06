def sort_age(lst):
    # Use Python's built-in sort with a key targeting the age (index 1 of the tuple)
    # reverse=True ensures older people (larger age) are at the front.
    lst.sort(key=lambda x: x[1], reverse=True)
    return lst
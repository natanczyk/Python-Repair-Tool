def sort_age(lst):
    # Sort the list of tuples based on the second element (age) in descending order.
    # sorted() returns a new list, and key=lambda x: x[1] specifies sorting by age.
    # reverse=True ensures the older people are at the front.
    return sorted(lst, key=lambda x: x[1], reverse=True)
def sort_age(lst):
    # Sort the list of tuples based on the second element (age) in descending order.
    # key=lambda x: x[1] tells Python to sort by the age.
    # reverse=True ensures the older people (higher age) are at the front.
    return sorted(lst, key=lambda x: x[1], reverse=True)
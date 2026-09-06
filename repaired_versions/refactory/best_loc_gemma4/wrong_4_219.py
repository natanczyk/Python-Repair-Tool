def sort_age(lst):
    # We need to sort the list of tuples based on the second element (age) in descending order.
    # The key lambda x: x[1] tells Python to sort by the age.
    # reverse=True ensures the older people are at the front.
    return sorted(lst, key=lambda x: x[1], reverse=True)
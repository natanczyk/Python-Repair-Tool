def sort_age(lst):
    # Sort the list of tuples by age in descending order
    # We use a stable sort, and since no two members have the same age,
    # we can simply sort by the second element (age) in reverse order.
    return sorted(lst, key=lambda x: x[1], reverse=True)
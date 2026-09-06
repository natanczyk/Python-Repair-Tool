def sort_age(lst):
    # Sort the list of tuples based on the second element (age) in descending order
    # lst.sort(key=lambda x: x[1], reverse=True) would modify the original list.
    # sorted() returns a new list.
    return sorted(lst, key=lambda x: x[1], reverse=True)
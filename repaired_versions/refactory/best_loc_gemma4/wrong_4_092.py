def sort_age(lst):
    # We need to sort the list of tuples based on the second element (age) in descending order.
    # The simplest and most efficient way in Python is using the sorted() function with a key.
    return sorted(lst, key=lambda x: x[1], reverse=True)
def sort_age(lst):
    # We need to sort the list of tuples based on the age (the second element of the tuple)
    # in descending order.
    # The most efficient way to do this in Python is using the sorted() function 
    # or the .sort() method with a custom key.
    return sorted(lst, key=lambda x: x[1], reverse=True)
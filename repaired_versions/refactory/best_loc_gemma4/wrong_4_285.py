def sort_age(lst):
    # Sort the list in-place by the second element of the tuple (age) in descending order
    lst.sort(key=lambda x: x[1], reverse=True)
    # Return the sorted list
    return lst
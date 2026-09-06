def sort_age(lst):
    # Sort the list based on the second element of the tuple (age) in descending order
    lst.sort(key=lambda x: x[1], reverse=True)
    return lst
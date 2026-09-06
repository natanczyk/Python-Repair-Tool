def sort_age(lst):
    # Sort the list by age (second element of tuple) in descending order
    return sorted(lst, key=lambda x: x[1], reverse=True)
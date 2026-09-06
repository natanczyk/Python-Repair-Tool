def sort_age(lst):
    # Sort the list of tuples by age (second element) in descending order
    return sorted(lst, key=lambda x: x[1], reverse=True)
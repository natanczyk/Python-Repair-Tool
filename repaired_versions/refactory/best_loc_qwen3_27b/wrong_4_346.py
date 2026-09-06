def sort_age(lst):
    # Sort the list of tuples by age (index 1) in descending order
    sorted_lst = sorted(lst, key=lambda x: x[1], reverse=True)
    return sorted_lst
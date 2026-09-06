def sort_age(lst):
    # Sort the list based on age in descending order
    sorted_lst = sorted(lst, key=lambda x: x[1], reverse=True)
    return sorted_lst
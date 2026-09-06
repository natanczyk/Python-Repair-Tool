def sort_age(lst):
    # Sort the list by age (second element of each tuple) in descending order
    sorted_lst = sorted(lst, key=lambda x: x[1], reverse=True)
    return sorted_lst
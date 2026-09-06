def sort_age(lst):
    # Sort the list of tuples by age in descending order
    # We use the second element of each tuple (age) as the key
    sorted_lst = sorted(lst, key=lambda x: x[1], reverse=True)
    return sorted_lst
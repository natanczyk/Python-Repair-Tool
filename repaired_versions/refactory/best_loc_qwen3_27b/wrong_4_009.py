def sort_age(lst):
    # Sort the list in descending order by age (the second element of each tuple)
    return sorted(lst, key=lambda x: x[1], reverse=True)
def sort_age(lst):
    # Sort the list by age in descending order
    # Since no two members have the same age, we can simply sort by the second element of each tuple
    return sorted(lst, key=lambda x: x[1], reverse=True)
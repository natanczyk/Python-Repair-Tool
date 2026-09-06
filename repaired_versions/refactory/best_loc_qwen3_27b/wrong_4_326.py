def sort_age(lst):
    if not lst:
        return []
    
    # Sort by age in descending order
    # Since no two members have the same age, we can simply sort by the second element of the tuple
    sorted_lst = sorted(lst, key=lambda x: x[1], reverse=True)
    return sorted_lst
def sort_age(lst):
    if not lst:
        return []
    
    # Sort by age in descending order
    sorted_lst = sorted(lst, key=lambda x: x[1], reverse=True)
    return sorted_lst
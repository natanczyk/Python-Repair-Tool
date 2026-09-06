def sort_age(lst):
    # Handle empty list case
    if not lst:
        return []
    
    # Sort the list by age in descending order
    # We use a stable sort, sorting by age descending
    sorted_lst = sorted(lst, key=lambda x: x[1], reverse=True)
    
    return sorted_lst
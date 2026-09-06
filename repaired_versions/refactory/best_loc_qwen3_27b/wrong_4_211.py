def sort_age(lst):
    # Create a copy to avoid modifying the original list if that matters,
    # but since we are returning a new list, we can work on a copy or just sort directly.
    # The problem asks to return a sorted list.
    # We can simply use Python's built-in sort with a key.
    
    # Sort by age (index 1) in descending order
    sorted_lst = sorted(lst, key=lambda x: x[1], reverse=True)
    
    return sorted_lst
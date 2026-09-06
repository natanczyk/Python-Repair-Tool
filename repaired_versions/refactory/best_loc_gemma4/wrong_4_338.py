def sort_age(lst):
    if not lst:
        return []
    
    # The goal is to sort by age in descending order.
    # The original logic was attempting a manual insertion sort but had bugs.
    # The simplest and most efficient way in Python is using sorted() with a key.
    return sorted(lst, key=lambda x: x[1], reverse=True)
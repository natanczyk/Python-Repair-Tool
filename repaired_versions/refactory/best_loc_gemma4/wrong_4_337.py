def sort_age(lst):
    if not lst:
        return []
    
    # The goal is to sort people by age in descending order.
    # The original buggy code attempted a manual insertion sort but had logic errors
    # and failed on empty lists.
    
    # We can use Python's built-in sorted function with a key targeting the age (index 1)
    # and reverse=True to put older people at the front.
    return sorted(lst, key=lambda x: x[1], reverse=True)
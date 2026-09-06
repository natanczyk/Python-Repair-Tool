def sort_age(lst):
    # Handle empty list case to avoid IndexError
    if not lst:
        return []
    
    # Use Python's built-in sorted function with a custom key
    # The key is the second element of the tuple (age)
    # reverse=True ensures older people (larger age) are at the front
    return sorted(lst, key=lambda x: x[1], reverse=True)
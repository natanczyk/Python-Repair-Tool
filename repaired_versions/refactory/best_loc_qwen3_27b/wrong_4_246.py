def sort_age(lst):
    # Handle empty list case
    if not lst:
        return []
    
    # Sort by age in descending order
    # We use a key that extracts the age (index 1) and reverse=True for descending
    return sorted(lst, key=lambda x: x[1], reverse=True)
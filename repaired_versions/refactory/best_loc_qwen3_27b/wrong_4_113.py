def sort_age(lst):
    # Handle empty list case
    if not lst:
        return []
    
    # Sort by age in descending order (older people first)
    # We use a stable sort, and since no two members have the same age,
    # we just need to sort by the second element (age) in reverse
    out = sorted(lst, key=lambda x: x[1], reverse=True)
    
    return out
def sort_age(lst):
    # Create a copy to avoid modifying the original list if needed, 
    # but since we're returning a sorted version, let's work on a copy or just sort properly
    result = lst[:]
    # Sort by age (index 1) in descending order
    result.sort(key=lambda x: x[1], reverse=True)
    return result
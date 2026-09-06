def sort_age(lst):
    if not lst:
        return []
    
    # The goal is to sort tuples by age (index 1) in descending order.
    # The original code attempted a manual insertion sort but had bugs.
    # The most efficient and Pythonic way is using the sorted() function.
    return sorted(lst, key=lambda x: x[1], reverse=True)
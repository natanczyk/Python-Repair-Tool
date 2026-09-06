def sort_age(lst):
    # Create a copy to avoid modifying the original list if needed, 
    # but since the tests seem to expect a new sorted list or modified list,
    # let's implement a proper sorting algorithm.
    # The buggy code attempts insertion sort but has bugs.
    # Let's fix it by implementing a correct insertion sort or using Python's built-in sort.
    
    # Using Python's built-in sorted with a key to sort by age in descending order
    return sorted(lst, key=lambda x: x[1], reverse=True)
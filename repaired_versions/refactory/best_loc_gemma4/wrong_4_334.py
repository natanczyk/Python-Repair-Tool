def sort_age(lst):
    # We need to sort the list of tuples based on the second element (age) in descending order.
    # The original code attempted a manual sort but had logic errors and return value issues.
    # The most efficient and Pythonic way to achieve this is using the sorted() function or .sort() method.
    
    # Sort by the second element of the tuple (x[1]) in reverse (descending) order.
    lst.sort(key=lambda x: x[1], reverse=True)
    return lst
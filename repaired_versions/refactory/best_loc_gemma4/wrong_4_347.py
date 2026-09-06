def sort_age(lst):
    # The goal is to sort the list of tuples by the second element (age) in descending order.
    # We use the sorted() function with a custom key that targets the age (index 1) 
    # and set reverse=True for descending order.
    return sorted(lst, key=lambda x: x[1], reverse=True)
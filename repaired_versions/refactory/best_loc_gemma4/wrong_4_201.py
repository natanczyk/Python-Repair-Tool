def sort_age(lst):
    # The goal is to sort tuples of (gender, age) by age in descending order.
    # The most efficient and Pythonic way to achieve this is using the sorted() function
    # with a custom key that targets the second element of the tuple (the age).
    return sorted(lst, key=lambda x: x[1], reverse=True)
def sort_age(lst):
    # The goal is to sort the list of tuples by age (the second element) in descending order.
    # We use the sorted() function with a custom key that targets the second element of each tuple.
    # reverse=True ensures that the older people (larger age) are at the front.
    return sorted(lst, key=lambda x: x[1], reverse=True)
def sort_age(lst):
    # The goal is to sort the list of tuples (gender, age) in descending order of age.
    # We use the sorted() function with a key that targets the second element of the tuple (index 1).
    # reverse=True ensures the older people (larger age) are at the front.
    return sorted(lst, key=lambda x: x[1], reverse=True)
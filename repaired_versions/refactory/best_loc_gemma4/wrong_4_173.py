def sort_age(lst):
    # We need to sort the list of tuples (gender, age) by age in descending order.
    # The most efficient way in Python is using the sorted() function with a key.
    # lambda x: x[1] tells Python to sort based on the second element of the tuple (the age).
    # reverse=True ensures that the older people (larger age) are at the front.
    return sorted(lst, key=lambda x: x[1], reverse=True)
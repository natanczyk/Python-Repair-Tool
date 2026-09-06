def sort_age(lst):
    # Sort the list based on the second element of the tuple (age)
    # reverse=True ensures that older people (larger age) are at the front
    return sorted(lst, key=lambda x: x[1], reverse=True)
def sort_age(lst):
    """
    Sorts a list of tuples (gender, age) in descending order of age.
    """
    # Using Python's built-in sorted function with a custom key.
    # key=lambda x: x[1] tells Python to sort based on the second element of the tuple (age).
    # reverse=True ensures the sorting is in descending order (older people first).
    return sorted(lst, key=lambda x: x[1], reverse=True)
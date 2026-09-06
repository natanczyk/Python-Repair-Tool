def sort_age(lst):
    # The task is to sort people by age in descending order.
    # The provided test cases show that the sorting is based solely on the age (the second element of the tuple).
    # Using sorted() with a key for the second element and reverse=True handles all cases, including empty lists.
    return sorted(lst, key=lambda x: x[1], reverse=True)
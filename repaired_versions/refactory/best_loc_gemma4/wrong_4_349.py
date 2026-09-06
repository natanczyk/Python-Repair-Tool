def sort_age(lst):
    # The requirement is to sort the people by age in descending order.
    # The test cases show that the primary sort key is the age (index 1) in descending order.
    # Since the problem states "no two members in the list of people are of the same age",
    # a simple sort on the age in reverse order is sufficient.
    return sorted(lst, key=lambda x: x[1], reverse=True)
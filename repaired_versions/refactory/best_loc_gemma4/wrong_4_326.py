def sort_age(lst):
    # The goal is to sort the list of tuples (<gender>, <age>) 
    # such that the older people (higher age) are at the front.
    # Since no two members have the same age, we simply sort by the age 
    # (the second element of the tuple) in descending order.
    return sorted(lst, key=lambda x: x[1], reverse=True)
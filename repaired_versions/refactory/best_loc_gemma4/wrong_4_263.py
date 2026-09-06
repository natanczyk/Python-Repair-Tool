def sort_age(lst):
    # Use sorted() to return a new list and reverse=True to sort by age in descending order
    return sorted(lst, key=lambda x: x[1], reverse=True)
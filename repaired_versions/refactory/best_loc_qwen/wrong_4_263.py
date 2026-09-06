def sort_age(lst):
    # Use sorted() instead of lst.sort() to return a new sorted list
    return sorted(lst, key=lambda x: x[1], reverse=True)
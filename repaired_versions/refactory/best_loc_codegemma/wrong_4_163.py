def sort_age(lst):
    lst = sorted(lst, key=lambda x: x[1], reverse=True)
    return lst
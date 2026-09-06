def sort_age(lst):
    a = sorted(lst, key=lambda x: x[1], reverse=True)
    return a
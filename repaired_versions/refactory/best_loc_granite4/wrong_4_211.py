def sort_age(lst):
    result = sorted(lst, key=lambda x: x[1], reverse=True)
    return result
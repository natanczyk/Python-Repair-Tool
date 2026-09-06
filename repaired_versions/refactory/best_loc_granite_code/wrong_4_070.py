def sort_age(lst):
    if len(lst) <= 1:
        return lst
    oldest = max(lst, key=lambda x: x[1])
    lst.remove(oldest)
    return [oldest] + sort_age(lst)
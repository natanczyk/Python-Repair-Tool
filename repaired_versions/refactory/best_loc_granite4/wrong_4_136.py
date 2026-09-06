def sort_age(lst):
    a = lst[:]
    sort = []
    while a:
        max_elem = max(a, key=lambda x: x[1])
        a.remove(max_elem)
        sort.append(max_elem)
    return sort
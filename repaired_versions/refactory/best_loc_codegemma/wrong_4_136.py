def sort_age(lst):
    a = lst
    sort = []
    if not a:
        return []
    smallest = a[0]
    while a:
        for element in a:
            if element[1] > smallest[1]:
                smallest = element
        sort.append(smallest)
        a.remove(smallest)
        smallest = a[0] if a else None
    return sort
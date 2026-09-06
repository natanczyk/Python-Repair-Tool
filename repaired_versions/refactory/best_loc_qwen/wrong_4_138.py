def sort_age(lst):
    sort = []
    while lst: # a is not []
        smallest = lst[0]
        for element in lst:
            if element[1] > smallest[1]:  # Change < to >
                smallest = element
        sort.append(smallest)
        lst.remove(smallest)
    return sort
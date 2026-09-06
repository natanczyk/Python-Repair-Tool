def sort_age(lst):
    sort = []
    while lst:
        largest = lst[0]
        for item in lst:
            if item[1] > largest[1]:
                largest = item
        lst.remove(largest)
        sort.append(largest)
    return sort
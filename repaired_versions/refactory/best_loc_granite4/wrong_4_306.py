def sort_age(lst):
    sort = []
    while lst:
        largest = lst[0]
        for i in lst:
            if i[1] > largest[1]:  # Compare based on age (second element)
                largest = i
        lst.remove(largest)
        sort.append(largest)
    return sort
def sort_age(lst):
    a = lst[:]  # Create a copy to avoid modifying the original list
    sort = []
    while a:
        largest = a[0]
        for item in a:
            if item[1] > largest[1]:
                largest = item
        a.remove(largest)
        sort.append(largest)
    return sort
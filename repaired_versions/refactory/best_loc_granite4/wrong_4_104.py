def sort_age(lst):
    sort1 = []
    while lst:
        largest = lst[0][1]
        largest_item = lst[0]
        for item in lst:
            if item[1] > largest:
                largest = item[1]
                largest_item = item
        lst.remove(largest_item)
        sort1.append(largest_item)
    return sort1
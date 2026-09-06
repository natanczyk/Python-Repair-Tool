def sort_age(lst):
    result = []
    while lst != []:
        largest = lst[0][1]
        largest_tup = lst[0]
        for i in lst:
            if i[1] > largest:
                largest = i[1]
                largest_tup = i
        lst.remove(largest_tup)
        result.append(largest_tup)
    return result
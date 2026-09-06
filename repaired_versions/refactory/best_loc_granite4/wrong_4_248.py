def sort_age(lst):
    list1 = []
    while lst:
        max_index = 0
        for i in range(1, len(lst)):
            if lst[i][1] > lst[max_index][1]:
                max_index = i
        list1.append(lst[max_index])
        lst.pop(max_index)
    return list1
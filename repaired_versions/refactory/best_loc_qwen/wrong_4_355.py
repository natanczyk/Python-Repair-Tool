def sort_age(lst):
    newlst = []
    while lst:
        maximum = lst[0][1]
        max_index = 0
        for i in range(len(lst)):
            if lst[i][1] > maximum:
                maximum = lst[i][1]
                max_index = i
        newlst.append(lst.pop(max_index))

    return newlst
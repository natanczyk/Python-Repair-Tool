def sort_age(lst):
    newlst = []
    while lst:
        max_tuple = lst[0]
        for element in lst:
            if element[1] > max_tuple[1]:
                max_tuple = element
        lst.remove(max_tuple)
        newlst.append(max_tuple)
    return newlst
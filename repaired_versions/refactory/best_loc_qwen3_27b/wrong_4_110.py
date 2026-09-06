def sort_age(lst):
    new = []
    while lst:
        largest = lst[0][1]
        for i in lst:
            if i[1] > largest:
                largest = i[1]
        tpl = None
        for j in lst:
            if j[1] == largest:
                tpl = j
                break
        lst.remove(tpl)
        new.append(tpl)
    return new
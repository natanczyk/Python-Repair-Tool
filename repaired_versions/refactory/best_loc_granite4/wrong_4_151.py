def sort_age(lst):
    new = []
    while lst:
        max_age = lst[0][1]
        max_name = lst[0][0]
        for ele in lst:
            if ele[1] > max_age:
                max_age = ele[1]
                max_name = ele[0]
        new.append((max_name, max_age))
        lst.remove((max_name, max_age))
    return new
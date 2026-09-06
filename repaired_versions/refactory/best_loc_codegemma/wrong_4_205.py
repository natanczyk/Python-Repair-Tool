def sort_age(lst):
    if not lst:
        return []
    max_age = max(lst, key=lambda x: x[1])[1]
    new_lst = []
    for i in lst:
        if i[1] == max_age:
            new_lst.append(i)
    for i in new_lst:
        lst.remove(i)
    return new_lst + sort_age(lst)
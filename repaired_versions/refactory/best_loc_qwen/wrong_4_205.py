def sort_age(lst):
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return lst
    else:
        used_lst = lst.copy()
        max_age = max([i[1] for i in lst])
        new_lst = [i for i in lst if i[1] == max_age]
        used_lst = [i for i in used_lst if i not in new_lst]
        return new_lst + sort_age(used_lst)
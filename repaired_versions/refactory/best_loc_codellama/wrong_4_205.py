def sort_age(lst):
    if not lst:
        return []
    else:
        used_lst = lst.copy()
        ages = []
        for i in lst:
            ages.append(i[1])
        max_age = max(ages)
        new_lst = [i for i in lst if i[1] == max_age]
        used_lst = [i for i in lst if i[1] != max_age]
        return new_lst + sort_age(used_lst)
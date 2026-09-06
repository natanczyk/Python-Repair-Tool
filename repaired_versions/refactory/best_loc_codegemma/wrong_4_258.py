def sort_age(lst):
    res = []
    age_list = []
    while lst:
        for i in lst:
            age_list.append(i[1])
        max_age = max(age_list)
        for i in lst:
            if i[1] == max_age:
                res.append(i)
        for i in lst:
            if i[1] == max_age:
                lst.remove(i)
        age_list.remove(max_age)
    return res
def sort_age(lst):
    res = []
    while lst:
        max_age = max([person[1] for person in lst])
        for i in lst:
            if i[1] == max_age:
                res.append(i)
        lst = [person for person in lst if person[1] != max_age]
    return res
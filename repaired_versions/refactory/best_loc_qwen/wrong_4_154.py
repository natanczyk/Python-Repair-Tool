def sort_age(lst):
    new = []
    while lst:
        max_age = max(lst, key=lambda x: x[1])[1]
        for ele in lst:
            if ele[1] == max_age:
                new.append(ele)
                lst.remove(ele)
                break
    return new
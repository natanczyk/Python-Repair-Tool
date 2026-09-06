def sort_age(lst):
    old_lst = lst.copy()
    new_lst = []
    while old_lst:
        largest = old_lst[0]
        for i in old_lst:
            if i[1] > largest[1]:
                largest = i
        old_lst.remove(largest)
        new_lst.append(largest)
    return new_lst
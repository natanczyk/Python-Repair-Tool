def sort_age(lst):
    new_lst = []
    for i in range(len(lst)):
        max_num = max(lst, key=lambda x: x[1])
        lst.remove(max_num)
        new_lst.append(max_num)
    return new_lst
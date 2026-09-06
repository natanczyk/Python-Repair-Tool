def sort_age(lst):
    new_list = []
    for i in lst:
        new_list.append(i)
    return sorted(new_list, key=lambda x: x[1], reverse=True)
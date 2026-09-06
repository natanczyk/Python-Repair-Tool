def sort_age(lst):
    sorted_lst = sorted(lst, key=lambda x: x[1], reverse=True)
    return sorted_lst
def sort_age(lst):
    sorted_list = sorted(lst, key=lambda x: x[1], reverse=True)
    return sorted_list
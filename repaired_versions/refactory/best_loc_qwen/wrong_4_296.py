def sort_age(lst):
    ages = [(item[1], item) for item in lst]
    sorted_lst = sorted(ages, reverse=True)
    return [item for _, item in sorted_lst]
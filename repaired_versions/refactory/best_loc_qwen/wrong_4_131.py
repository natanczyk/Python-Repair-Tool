def sort(lst):
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[i][1] < lst[j][1]:  # Change from > to < for descending order
                lst[i], lst[j] = lst[j], lst[i]
    return lst

def sort_age(lst):
    return sort(lst)
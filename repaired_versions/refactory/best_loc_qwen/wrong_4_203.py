def sort_age(lst):
    sort = []
    while len(lst) > 0:
        smallest = lst[0]
        for i in lst:
            if i[1] > smallest[1]:  # Change from < to >
                smallest = i  # Assign the entire tuple, not just the age

        lst.remove(smallest)
        sort.append(smallest)
    return sort
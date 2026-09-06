def sort_age(lst):
    sorted_lst = []
    while lst:
        smallest = lst[0]
        for i in lst:
            if i[1] > smallest[1]:  # Change comparison operator to find the maximum value
                smallest = i
        lst.remove(smallest)
        sorted_lst.append(smallest)
    return sorted_lst
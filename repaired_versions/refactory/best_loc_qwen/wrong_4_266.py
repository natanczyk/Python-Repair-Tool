def sort_age(lst):
    sorted_list = []
    while lst:
        smallest = lst[0]
        for x in lst:
            if x[1] > smallest[1]:  # Change < to > to sort by descending age
                smallest = x
        sorted_list.append(smallest)
        lst.remove(smallest)
    return sorted_list
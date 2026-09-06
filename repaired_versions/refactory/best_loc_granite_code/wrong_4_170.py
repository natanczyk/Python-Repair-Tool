def sort_age(lst):
    sorted_lst = []
    while lst:
        largest = lst[0]
        for i in lst:
            if i[1] > largest[1]:
                largest = i
        lst.remove(largest)
        sorted_lst.append(largest)
    return sorted_lst
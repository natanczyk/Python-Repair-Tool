def sort_age(lst):
    sort_list = []
    while lst: # lst is not empty
        largest = lst[0]
        for element in lst:
            if element[1] > largest[1]:
                largest = element
        lst.remove(largest)
        sort_list.append(largest)
    return sort_list
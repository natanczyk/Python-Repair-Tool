def sort_age(lst):
    sorted_list = []
    while lst:
        largest = lst[0]
        for item in lst:
            if item[1] > largest[1]:
                largest = item
        lst.remove(largest)
        sorted_list.append(largest)
    return sorted_list
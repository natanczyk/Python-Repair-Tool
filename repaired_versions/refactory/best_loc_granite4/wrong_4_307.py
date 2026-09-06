def sort_age(lst):
    sorted_list = []
    while lst:
        largest = lst[0]
        for i in lst:
            if i[1] > largest[1]:  # Compare based on age (second element)
                largest = i
        lst.remove(largest)
        sorted_list.append(largest)
    return sorted_list
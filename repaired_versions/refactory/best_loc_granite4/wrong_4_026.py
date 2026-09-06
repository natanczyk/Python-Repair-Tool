def sort_age(lst):
    sorted_list = []
    while lst: 
        biggest = lst[0]
        for element in lst:
            if element[1] > biggest[1]:  # Compare based on age (second element of the tuple)
                biggest = element
        lst.remove(biggest)
        sorted_list.append(biggest)
    return sorted_list
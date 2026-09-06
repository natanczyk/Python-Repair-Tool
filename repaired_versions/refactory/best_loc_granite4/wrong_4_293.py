def sort_age(lst):
    sorted_list = []
    while lst:
        biggest = lst[0]  # Initialize with the first element
        for i in lst:
            if i[1] > biggest[1]:
                biggest = i
        lst.remove(biggest)
        sorted_list.append(biggest)
    return sorted_list
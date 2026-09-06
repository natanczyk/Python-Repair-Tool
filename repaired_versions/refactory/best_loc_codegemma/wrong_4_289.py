def sort_age(lst):
    new_list=[]
    largest=0
    while lst:
        largest=0
        for i in lst:
            if i[1]>largest:
                largest = i[1]
                largest_tuple = i
        new_list.append(largest_tuple)
        lst.remove(largest_tuple)
    return new_list
def sort_age(lst):
    
    sort_lst = []
    
    while lst:
        largest = lst[0]
        for element in lst:
            if element[1] > largest[1]:
                largest = element
        lst.remove(largest)
        sort_lst.append(largest)
    return sort_lst
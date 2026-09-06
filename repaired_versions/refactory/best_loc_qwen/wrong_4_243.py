def sort_age(lst):
    if not lst:
        return []
    
    sorted_lst = []
    while lst:
        smallest = lst[0]
        for item in lst:
            if item[1] > smallest[1]:
                smallest = item
        sorted_lst.append(smallest)
        lst.remove(smallest)
    
    return sorted_lst
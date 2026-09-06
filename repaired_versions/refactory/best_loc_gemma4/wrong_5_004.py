def top_k(lst, k):
    # Handle the case where k is 0 immediately
    if k <= 0:
        return []
        
    # Create a copy of the list to avoid modifying the original input list
    lst_copy = list(lst)
    sort = []
    while lst_copy: 
        biggest = lst_copy[0]
        for element in lst_copy:
            if element > biggest:
                biggest = element
                
        lst_copy.remove(biggest)
        sort.append(biggest)
        if len(sort) == k:
            break
    return sort
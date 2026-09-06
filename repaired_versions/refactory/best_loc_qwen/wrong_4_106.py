def sort_age(lst):
    if not lst:
        return []
    
    sort = []
    while lst:
        smallest = lst[0]
        for k in lst:
            if k[1] > smallest[1]:  # Change from < to > for descending order
                smallest = k
        sort.append(smallest)
        lst.remove(smallest)  # Remove the found smallest element from the original list
    
    return sort
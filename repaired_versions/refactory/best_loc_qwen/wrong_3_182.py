def remove_extras(lst):
    a = []
    for j in range(len(lst)):
        if lst[j] not in a:
            a.append(lst[j])
    
    return a
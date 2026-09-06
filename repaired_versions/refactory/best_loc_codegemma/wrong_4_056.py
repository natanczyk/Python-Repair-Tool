def sort_age(lst):
    # Fill in your code here
    new_lst = []
    if not lst:
        return []
    oldest = lst[0]
    for i in range(len(lst)):
        if lst[i][1] > oldest[1]:
            oldest = lst[i] 
    new_lst.append(oldest)
    lst.remove(oldest)
    
    while lst:
        oldest = lst[0]
        for i in range(len(lst)):
            if lst[i][1] > oldest[1]:
                oldest = lst[i] 
        new_lst.append(oldest)
        lst.remove(oldest)
        
    return new_lst
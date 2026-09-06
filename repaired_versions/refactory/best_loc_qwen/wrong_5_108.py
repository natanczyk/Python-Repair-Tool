def top_k(lst, k):
    new_lst = []
    counter = 0
    while counter < k:
        highest = lst[0]  # initialize highest with the first element
        for x in lst:
            if x > highest:
                highest = x
        new_lst.append(highest)
        lst.remove(highest)
        counter += 1
        
    return new_lst
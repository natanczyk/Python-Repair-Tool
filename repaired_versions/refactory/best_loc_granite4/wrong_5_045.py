def top_k(lst, k):
    newlst = []
    while len(newlst) < k and lst:  # Ensure we don't exceed k and lst is not empty
        maximum = lst[0]
        for i in lst:
            if i > maximum:
                maximum = i
        newlst.append(maximum)
        lst.remove(maximum)
    return newlst
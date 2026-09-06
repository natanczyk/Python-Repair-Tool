def top_k(lst, k):
    newlst = []
    for i in range(k):
        if lst:  # Ensure the list is not empty
            newlst.append(max(lst))
            lst.remove(max(lst))
    return newlst
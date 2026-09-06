def top_k(lst, k):
    new_list = []
    for i in range(k):
        if k==0:
            break
        new_list.append(max(lst))
        lst.remove(max(lst))
        k -= 1
    return new_list
    pass
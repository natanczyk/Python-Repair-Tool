def top_k(lst, k):
    arranged = []
    while k > 0:
        max_num = max(lst)
        arranged.append(max_num)
        lst.remove(max_num)
        k = k-1
    return arranged
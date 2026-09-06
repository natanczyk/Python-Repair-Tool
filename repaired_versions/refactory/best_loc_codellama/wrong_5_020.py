def top_k(lst, k):
    arranged = []
    for i in range(k):
        max_value = max(lst)
        arranged.append(max_value)
        lst.remove(max_value)
    return arranged
def top_k(lst, k):
    newlist = []
    while len(newlist) < k:
        max_value = max(lst)
        for i in range(len(lst)):
            if lst[i] == max_value:
                newlist.append(max_value)
                del lst[i]
                break
    return newlist
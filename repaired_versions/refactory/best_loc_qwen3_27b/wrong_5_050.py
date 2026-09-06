def top_k(lst, k):
    newlist = []
    lst = lst.copy()  # Avoid modifying the original list
    while len(newlist) < k:
        max_val = max(lst)
        newlist.append(max_val)
        # Remove the first occurrence of max_val from lst
        for i in range(len(lst)):
            if lst[i] == max_val:
                del lst[i]
                break
    return newlist
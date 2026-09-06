def top_k(lst, k):
    if lst == []:
        return []
    elif k == 0:
        return []
    else:
        # Create a copy of the list to avoid mutating the original input
        temp_lst = list(lst)
        final = []
        while temp_lst:
            element = max(temp_lst)
            final += [element,]
            temp_lst.remove(element)
            if len(final) == k:
                break
        return final
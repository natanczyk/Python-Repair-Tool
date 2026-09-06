def top_k(lst, k):
    if lst == [] or k == 0:
        return []
    else:
        final = []
        # Create a copy of the list to avoid mutating the original input
        temp_lst = list(lst)
        while temp_lst:
            element = max(temp_lst)
            final += [element,]
            temp_lst.remove(element)
            if len(final) == k:
                break
        return final
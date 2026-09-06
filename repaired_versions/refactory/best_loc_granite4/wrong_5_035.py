def top_k(lst, k):
    if lst == [] or k == 0:
        return []
    else:
        final = []
        while lst:
            if len(final) == k:
                break
            element = max(lst)
            final.append(element)
            lst.remove(element)
        return final
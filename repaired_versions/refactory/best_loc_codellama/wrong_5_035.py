def top_k(lst, k):
    if lst == []:
        return []
    else:
        final = []
        while lst:
            element = max(lst)
            if len(final) == k:
                break
            final += [element,]
            lst.remove(element)
        return sorted(final, reverse=True)
def top_k(lst, k):
    final = []
    while len(final) < k:
        element = max(lst)
        final += [element,]
        lst.remove(element)
    return sorted(final, reverse=True)
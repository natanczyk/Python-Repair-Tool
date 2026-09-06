def top_k(lst, k):
    final = []
    while lst and k > 0:
        element = max(lst)
        final += [element,]
        lst.remove(element)
        k -= 1
    return sorted(final, reverse=True)
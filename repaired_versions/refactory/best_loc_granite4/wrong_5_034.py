def top_k(lst, k):
    final = []
    if k == 0:
        return final
    while lst:
        element = max(lst)
        final.append(element)
        lst.remove(element)
        if len(final) == k:
            break
    return final
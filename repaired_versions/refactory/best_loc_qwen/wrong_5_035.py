def top_k(lst, k):
    if lst == []:
        return []
    else:
        final = []
        while lst and len(final) < k:
            element = max(lst)
            final.append(element)
            lst.remove(element)
        return sorted(final, reverse=True)
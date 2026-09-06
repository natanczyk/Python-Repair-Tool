def top_k(lst, k):
    final = []
    while lst and len(final) < k:
        largest = max(lst)
        lst.remove(largest)
        final.append(largest)
    return final
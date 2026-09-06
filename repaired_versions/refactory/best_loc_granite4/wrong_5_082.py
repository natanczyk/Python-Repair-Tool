def top_k(lst, k):
    sotsot = []
    while lst and len(sotsot) < k:
        max_val = max(lst)
        sotsot.append(max_val)
        lst.remove(max_val)
    return sotsot
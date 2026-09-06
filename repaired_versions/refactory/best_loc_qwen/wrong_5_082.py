def top_k(lst, k):
    sotsot = []
    while lst and len(sotsot) < k:
        sotsot.append(max(lst))
        lst.remove(max(lst))
    return sorted(sotsot, reverse=True)
def top_k(lst, k):
    sotsot = []
    while lst and k > 0:
        max_val = max(lst)
        sotsot.append(max_val)
        lst.remove(max_val)
        k -= 1
    return sorted(sotsot, reverse=True)
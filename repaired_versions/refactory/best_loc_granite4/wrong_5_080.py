def top_k(lst, k):
    sotsot = []
    while len(sotsot) < k and lst:  # Ensure we don't exceed k and handle empty lst
        max_val = max(lst)
        sotsot.append(max_val)
        lst.remove(max_val)
    return sotsot
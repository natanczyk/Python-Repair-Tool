def top_k(lst, k):
    final = []
    lst = lst.copy()  # Avoid modifying the original list
    while lst and len(final) < k:
        largest = lst[0]
        for element in lst:
            if element > largest:
                largest = element
        lst.remove(largest)
        final.append(largest)
    return final
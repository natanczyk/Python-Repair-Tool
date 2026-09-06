def top_k(lst, k):
    final = []
    if not lst or k == 0:
        return final
    while len(final) < k:
        largest = lst[0]
        for element in lst:
            if element > largest:
                largest = element
        final.append(largest)
        lst.remove(largest)
    return final
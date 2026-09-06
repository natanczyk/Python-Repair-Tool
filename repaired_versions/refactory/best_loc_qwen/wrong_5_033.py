def top_k(lst, k):
    final = []
    while lst and k > 0:
        largest = lst[0]
        for element in lst:
            if element > largest:
                largest = element
        lst.remove(largest)
        final.append(largest)
        k -= 1
    final.sort(reverse=True)
    return final
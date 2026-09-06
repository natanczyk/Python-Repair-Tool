def top_k(lst, k):
    sorted_list = []
    while lst and len(sorted_list) < k:
        largest = lst[0]
        for element in lst:
            if element > largest:
                largest = element
        lst.remove(largest)
        sorted_list.append(largest)
    return sorted_list
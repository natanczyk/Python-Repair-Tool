def top_k(lst, k):
    result = []
    while lst and len(result) < k:
        biggest = lst[0]
        for i in lst[1:]:
            if i > biggest:
                biggest = i
        lst.remove(biggest)
        result.append(biggest)
    
    return result
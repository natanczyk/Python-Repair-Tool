def top_k(lst, k):
    result = []
    while lst and len(result) < k:
        biggest = lst[0]
        for element in lst:
            if element > biggest:
                biggest = element
                
        lst.remove(biggest)
        result.append(biggest)
        
    return result
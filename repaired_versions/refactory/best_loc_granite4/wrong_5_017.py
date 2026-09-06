def top_k(lst, k):
    result = []
    while lst and len(result) < k:
        biggest = lst[0]
        for number in lst:
            if number > biggest:
                biggest = number
        lst.remove(biggest)
        result.append(biggest)
    return result
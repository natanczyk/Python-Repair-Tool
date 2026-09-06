def top_k(lst, k):
    rs = []
    for _ in range(k):
        if not lst:  # Handle case where k > len(lst)
            break
        biggest = lst[0]
        for num in lst:
            if biggest < num:
                biggest = num
        rs.append(biggest)
        lst.remove(biggest)
    return rs
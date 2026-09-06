def top_k(lst, k):
    rs = []
    # Make a copy to avoid modifying the original list
    lst_copy = lst[:]
    for _ in range(0, k):
        if not lst_copy:
            break
        biggest = lst_copy[0]
        for val in lst_copy:
            if val > biggest:
                biggest = val
        rs.append(biggest)
        lst_copy.remove(biggest)
    return rs
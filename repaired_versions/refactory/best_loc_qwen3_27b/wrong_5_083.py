def top_k(lst, k):
    result = []
    # Work on a copy to avoid modifying the original list and to handle iteration safely
    working_lst = lst[:]
    for i in range(k):
        if not working_lst:
            break
        largest = working_lst[0]
        for element in working_lst:
            if element > largest:
                largest = element
        working_lst.remove(largest)
        result.append(largest)
    return result
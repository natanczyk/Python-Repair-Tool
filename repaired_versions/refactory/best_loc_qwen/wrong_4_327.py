def sort_age(lst):
    sorted_lst = []
    while lst:
        oldest = lst[0]
        for i in range(len(lst)):
            if lst[i][1] > oldest[1]:
                oldest = lst[i]
        sorted_lst.append(oldest)
        lst.remove(oldest)
    return sorted_lst
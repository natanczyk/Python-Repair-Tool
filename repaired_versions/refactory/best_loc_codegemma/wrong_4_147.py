def sort_age(lst):
    sorted = []
    while lst:
        oldest = lst[0]
        for elem in lst:
            if elem[1] > oldest[1]:
                oldest = elem
        print(oldest)
        lst.remove(oldest)
        sorted.append(oldest)
    return sorted
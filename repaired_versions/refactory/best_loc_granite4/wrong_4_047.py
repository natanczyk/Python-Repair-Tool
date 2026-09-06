def sort_age(lst):
    output = []
    while lst:
        oldest = lst[0]
        for i in lst:
            if i[1] > oldest[1]:
                oldest = i
        lst.remove(oldest)
        output.append(oldest)
    return output
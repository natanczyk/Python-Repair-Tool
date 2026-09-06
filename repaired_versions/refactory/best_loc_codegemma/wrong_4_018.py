def sort_age(lst):
    if not lst:
        return []
    for i in range(1, len(lst)):
        j = i
        while j > 0 and lst[j][1] > lst[j - 1][1]:
            lst[j], lst[j - 1] = lst[j - 1], lst[j]
            j -= 1
    return lst
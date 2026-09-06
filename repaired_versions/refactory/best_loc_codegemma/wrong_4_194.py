def sort_age(lst):
    if not lst:
        return []
    biggest = lst[0]
    for i in range(1, len(lst)):
        if lst[i][1] > biggest[1]:
            biggest = lst[i]
    lst.remove(biggest)
    return [biggest] + sort_age(lst)
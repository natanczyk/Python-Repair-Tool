def sort_age(lst):
    if len(lst) <= 1:
        return lst
    else:
        biggest = lst[0]
        for i in range(1, len(lst)):
            if lst[i][1] > biggest[1]:
                biggest = lst[i]
        return [biggest] + sort_age([x for x in lst if x != biggest])
def sort_age(lst):
    n = len(lst)
    for _ in range(n):
        for i in range(n - 1):
            if lst[i][1] < lst[i+1][1]:
                x = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = x
    return lst
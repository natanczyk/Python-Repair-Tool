def sort_age(lst):
    for i in range(0,len(lst)):
        for j in range(0,len(lst)-i-1):
            if lst[j][1]<lst[j+1][1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst
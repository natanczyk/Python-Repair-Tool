def sort_age(lst):
    for i in range(0,len(lst)):
        for j in range(i+1,len(lst)):
            if lst[j][1]>lst[i][1]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst
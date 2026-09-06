def sort_age(lst):
    for i in range(len(lst)):
        smallest = lst[i][1]
        index = i
        for j in range(i+1, len(lst)):
            if lst[j][1] > smallest:
                smallest = lst[j][1]
                index = j
        lst[i], lst[index] = lst[index], lst[i]
    return lst
def sort_age(lst):
    new = []
    while lst:
        largest = lst[0]
        largest_index = 0
        for i in range(1, len(lst)):
            if lst[i][1] > largest[1]:
                largest = lst[i]
                largest_index = i
        lst.pop(largest_index)
        new.append(largest)
    return new
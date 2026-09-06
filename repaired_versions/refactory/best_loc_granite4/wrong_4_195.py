def sort_age(lst):
    new = []
    while lst:
        largest = lst[0]  # start with the first element as the largest
        for i in lst:
            if i[1] > largest[1]:
                largest = i
        lst.remove(largest)
        new.append(largest)
    return new
def sort_age(lst):
    s = []
    while lst:
        largest = lst[0]
        for element in lst:
            if element[1] > largest[1]:
                largest = element
        lst.remove(largest)
        s.append(largest)
    return s
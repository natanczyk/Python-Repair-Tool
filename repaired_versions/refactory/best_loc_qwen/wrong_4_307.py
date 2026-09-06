def sort_age(lst):
    sort = []
    while lst:
        largest = lst[0]
        for i in lst:
            if i[1] > largest[1]:  # Compare the second element (age) of the tuple
                largest = i
        lst.remove(largest)
        sort.append(largest)
    return sort
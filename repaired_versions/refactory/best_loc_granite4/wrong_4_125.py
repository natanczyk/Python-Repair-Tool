def sort_age(lst):
    lst1 = []
    while lst:
        largest = lst[0]
        for ele in lst:
            if ele[1] > largest[1]:
                largest = ele
        lst.remove(largest)
        lst1.append(largest)
    return lst1
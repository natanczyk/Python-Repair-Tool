def sort_age(lst):
    list1 = []
    while lst:
        biggest = lst[0]
        for i in range(1, len(lst)):
            if lst[i][1] > biggest[1]:
                biggest = lst[i]
        list1.append(biggest)
        lst.remove(biggest)
    return list1
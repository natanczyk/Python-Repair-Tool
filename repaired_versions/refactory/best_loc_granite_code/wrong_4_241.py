def sort_age(lst):
    list1 = []
    for i in range(len(lst)):
        list1.append(lst[i])
    list1.sort(key=lambda x: x[1], reverse=True)
    return list1
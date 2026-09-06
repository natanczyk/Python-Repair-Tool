def sort_age(lst):
    result = []
    while lst !=[]:
        highest = lst[0][1]
        index = 0
        for i in range(1,len(lst)):
            if lst[i][1]>highest:
                index = i
                highest = lst[i][1]
        result = result +[lst[index]]
        lst.pop(index)
    return result
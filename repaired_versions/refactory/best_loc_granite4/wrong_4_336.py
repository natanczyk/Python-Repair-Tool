def sort_age(lst):
    if len(lst) <= 1:  # Handle both empty list and single-element list
        return lst
    else:
        temp = lst[0][1]
        count = 0
        for i in range(len(lst)):
            if lst[i][1] > temp:
                temp = lst[i][1]
                count = i
        result = [lst[count],]
        lst.pop(count)
        return result + sort_age(lst)
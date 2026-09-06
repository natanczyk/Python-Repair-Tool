def sort_age(lst):
    def for_age(lst):
        for i in range(1, len(lst)):
            current = lst[i]
            j = i - 1
            while j >= 0 and lst[j][1] < current[1]:
                lst[j + 1] = lst[j]
                j -= 1
            lst[j + 1] = current
    
    for_age(lst)
    return lst
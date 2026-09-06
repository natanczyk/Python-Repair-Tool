def sort_age(lst):
    if len(lst) == 1:
        return lst
    else:
        new_list = []
        while lst:
            maximum = lst[0]
            for i in lst:
                if i[1] > maximum[1]:
                    maximum = i
            new_list.append(maximum)
            lst.remove(maximum)
        return new_list
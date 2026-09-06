def sort_age(lst):
    if len(lst) <= 1:
        return lst
    else:
        # Create a copy of the list to avoid modifying the original input
        temp_lst = list(lst)
        new_list = []
        while temp_lst:
            # We want the older people at the front, so we find the maximum age
            maximum = temp_lst[0]
            for i in temp_lst:
                if i[1] > maximum[1]:
                    maximum = i
            new_list.append(maximum)
            temp_lst.remove(maximum)
        return new_list
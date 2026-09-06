def sort_age(lst):
    output = []
    # Create a copy of the list to avoid modifying the original input list
    temp_lst = list(lst)
    while temp_lst:
        # We want the older people at the front, so we find the maximum age
        largest = temp_lst[0]
        for i in temp_lst:
            if i[1] > largest[1]:
                largest = i
        temp_lst.remove(largest)
        output.append(largest)
    return output
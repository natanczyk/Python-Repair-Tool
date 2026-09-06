def remove_extras(lst):
    i = 0
    while i < len(lst):
        j = i + 1
        while j < len(lst):
            if lst[i] == lst[j]:
                lst = lst[:j] + lst[j+1:]
                # Do not increment j here, because the next element 
                # has shifted into the current index j.
            else:
                j += 1
        i += 1
    return lst
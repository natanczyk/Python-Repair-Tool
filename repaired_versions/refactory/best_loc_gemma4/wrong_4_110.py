def sort_age(lst):
    new = []
    # Create a copy of the list to avoid modifying the original input list
    lst_copy = list(lst)
    while lst_copy:
        largest = lst_copy[0][1]
        for i in lst_copy:
            if i[1] > largest:
                largest = i[1]
        
        # Find the tuple that has the largest age
        target_tpl = None
        for j in lst_copy:
            if j[1] == largest:
                target_tpl = j
                break
        
        # Remove the identified tuple from the working list and add it to the result
        lst_copy.remove(target_tpl)
        new.append(target_tpl)
    return new
def sort_age(lst):
    newlst = []
    while lst:
        current = lst[0]
        for element in lst:
            if element[1] > current[1]:  # Change to find maximum age
                current = element
        newlst.append(current)  # Use append to add the tuple as a single element
        lst.remove(current)
    return newlst
def sort_age(lst):
    newlst = []
    while lst:
        current = lst[0]
        for element in lst:
            if element[1] > current[1]:  # Change to > for descending order
                current = element
        newlst.append(current)  # Use append instead of += (tuple syntax error)
        lst.remove(current)
    return newlst
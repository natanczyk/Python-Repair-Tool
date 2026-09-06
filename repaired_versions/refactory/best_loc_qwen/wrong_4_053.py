def sort_age(lst):
    newlst = []
    while lst:
        current = lst[0]
        for element in lst:
            if element[1] > current[1]:  # Change from < to >
                current = element
        newlst.append(current)  # Change from newlst += current to newlst.append(current)
        lst.remove(current)
    return newlst
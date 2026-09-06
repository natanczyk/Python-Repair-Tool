def remove_extras(lst):
    newlist = []
    for element in lst:
        if element not in newlist:
            newlist.append(element)
    return newlist
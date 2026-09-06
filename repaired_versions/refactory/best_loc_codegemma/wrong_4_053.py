def sort_age(lst):
    newlst = []
    while lst:
        current = lst[0]
        for element in lst:
            if element[1] > current[1]:  # Fix: Comparison for descending order
                current = element
        newlst.append(current)  # Fix: Append the tuple as a single object
        lst.remove(current)
    return newlst
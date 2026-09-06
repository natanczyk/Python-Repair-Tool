def remove_extras(lst):
    listt = lst.copy()
    listt.reverse()
    for element in listt[:]:
        if listt.count(element) > 1:
            listt.remove(element)
    listt.reverse()
    return listt
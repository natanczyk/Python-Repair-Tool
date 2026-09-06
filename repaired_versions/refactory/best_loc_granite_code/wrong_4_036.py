def sort_age(lst):
    """selection sort"""
    l = len(lst)
    for i in range(l):
        largest = i
        for j in range(i+1,l):
            if lst[j][1] > lst[largest][1]:
                largest = j #assign new largest index
        lst[i], lst[largest] = lst[largest], lst[i] #swap positions if larger
    return lst
def sort_age(lst):
    sort = [] # empty list
    while lst:
        largest = lst[0] # let the first element be the largest first
        for i in lst:
            if i[1] > largest[1]:
                largest = i
        lst.remove(largest) # use .remove() to remove the largest element
        sort.append(largest) # append the largest element to the sorted list
    return sort
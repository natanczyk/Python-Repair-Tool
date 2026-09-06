def sort_age(lst):
    result = []
    while lst:
        largest = lst[0]
        for element in lst:
            if element[1] > largest[1]:
                largest = element
        lst.remove(largest)
        result.append(largest)
    return result
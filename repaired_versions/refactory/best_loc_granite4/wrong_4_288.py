def sort_age(lst):
    sort = []
    while lst:
        largest = lst[0]  # Initialize largest with the first element of lst
        for element in lst:  # Iterate over lst, not a
            if element[1] > largest[1]:  # Compare based on age (second element of tuple)
                largest = element
        lst.remove(largest)
        sort.append(largest)
    return sort  # Return the sorted list instead of printing lst
def sort_age(lst):
    # We create a copy of the list to avoid modifying the original input list
    a = list(lst)
    sorted_list = []
    
    while a:
        # Initialize the largest element as the first element of the current list
        largest = a[0]
        for element in a:
            # Compare the age (index 1 of the tuple)
            if element[1] > largest[1]:
                largest = element
        
        # Remove the found largest element from the temporary list and add to result
        a.remove(largest)
        sorted_list.append(largest)
        
    return sorted_list
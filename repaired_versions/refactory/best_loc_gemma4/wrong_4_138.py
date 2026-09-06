def sort_age(lst):
    # Create a copy of the list to avoid modifying the original input list
    people = list(lst)
    sorted_list = []
    
    while people:
        # We want the older people at the front, so we find the maximum age
        largest = people[0]
        for element in people:
            if element[1] > largest[1]:
                largest = element
        
        # Remove the found person from the temporary list and add to the result
        people.remove(largest)
        sorted_list.append(largest)
        
    return sorted_list
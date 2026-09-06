def sort_age(lst):
    # Create a copy of the list to avoid mutating the original input
    people = list(lst)
    sorted_lst = []
    while people:
        # Find the person with the maximum age
        largest = people[0]
        for i in people:
            if i[1] > largest[1]:
                largest = i
        # Remove the found person from the temporary list and add to sorted list
        people.remove(largest)
        sorted_lst.append(largest)
    return sorted_lst